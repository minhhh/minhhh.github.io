Title: Unity singleton
Date: 2016-09-22 00:00
Author: Ha.Minh
Category: Unity
Tags: unity, singleton
Status: draft


First of all, please remember that Singletons are generally not recommended due to various obvious disadvantages:
* Hard to reason about code
* Encourage coupling
* Potential concurrency issue

However, in game development it's super useful to have singleton for many types of global system, including but not limited to:
* Sound system
* Time manager
* Localization
* Tutorial
* Login
* Global Notifier

In this article we will look at some options of Singleton implementation we have in Unity to see what problems they're trying to solve and what assumptions they made.

## Requirements
Let's first review some requirements for a useful singleton system in Unity.

**Singleton class types**
* MonoBehavior based: These types of singletons extends MonoBehavior and shows themselves in the scene hierarchy so that you can look at their exposed members. Another reason is you want them to have an `Update` function to do something useful in it.
* Non MonoBehavior based: Traditional singletons in any OO languages. These singletons don't need to be inspected in the scene nor do they need `Update`.

**Singleton lifecycle types**
* Has dependencies: These singletons depend on other system or singletons to exist before they can start
* No dependencies: These singletons can be created anytime without waiting for any other entities.

**Singleton configurability types**
* Has customized parameters: This is a bit overlap with `Has dependencies` singletons. These singletons might: 1. Depends on parameters provided by another system, such as the FileSystem to load certian parameters from disk. OR 2. Need customized parameters or linked prefab. They might be in a prefab themselves such as a LevelManager.
* No customized parameters: These singletons behave the same all the time.


## Solutions
Fortunately there're already some solutions written in [unity3d](http://wiki.unity3d.com) so we can review and improve them as we wish.

### AManagerClass
[AManagerClass](http://wiki.unity3d.com/index.php/AManagerClass) is a standard implementation which supports MonoBehavior-based singletons. In the code, we refer to the singleton like this:
```
    AManager.instance.Foo ();
```

The `instance` function implementation is as below:
```
    public static AManager instance {
        get {
            if (s_Instance == null) {
                // This is where the magic happens.
                //  FindObjectOfType(...) returns the first AManager object in the scene.
                s_Instance =  FindObjectOfType(typeof (AManager)) as AManager;
            }

            // If it is still null, create a new instance
            if (s_Instance == null) {
                GameObject obj = new GameObject("AManager");
                s_Instance = obj.AddComponent(typeof (AManager)) as AManager;
                Debug.Log ("Could not locate an AManager object. \ AManager was Generated Automaticly.");
            }

            return s_Instance;
        }
    }
```

There are several problems with `AManager`:
* We have to duplicate it for all singleton class
* It's slow due to the 2 checks

Surely we can do better!

### AutoSingletonManager
* [AutoSingletonManager](http://wiki.unity3d.com/index.php/AutoSingletonManager) solves the code duplication problem of `AManager`

Here's the main code

```
public abstract class AutoSingletonManager : MonoBehaviour { }

public abstract class AutoSingletonManager<T> : AutoSingletonManager where T : AutoSingletonManager
{
    private static bool Compare<T>(T x, T y) where T : class
    {
        return x == y;
    }

    #region Singleton

    private static T _instance = default(T);

    public static T Instance
    {
        get
        {
            if (!Compare<T>(default(T), _instance)) return _instance;

            InitInstance(true);
            return _instance;
        }
    }

    #endregion

    public void Awake()
    {
        InitInstance(false);
    }

    public static void InitInstance(bool shouldInitManager)
    {
        Type thisType = typeof (T);

        _instance = FindObjectOfType<T>();

        if (Compare<T>(default(T), _instance))
        {
            _instance = new GameObject(thisType.Name).AddComponent<T>();
        }

        //Won't call InitManager from Awake
        if (shouldInitManager)
        {
            (_instance as AutoSingletonManager<T>).InitManager();
        }
    }

    public virtual void InitManager() { }
}
```

The code uses recursive generic definition. This allow us to reuse code by inheriting from the singleton class as well as from `MonoBehaviour`. Note that we don't have to make `AutoSingletonManager<T>` inherits from ` AutoSingletonManager`, instead we can make it inherit from our own class which in turn inherits from MonoBehavior.

It supports initializing the instance from `Awake` so maybe it can be used by adding directly it to an object in the scene. However, `InitManager` is not called in `Awake` so if you call `AutoSingletonManager.Instance` after it already awakes then InitManager will never be called.

Another more subtle draw back is it uses an unnecessary comparison `if (!Compare<T>(default(T), _instance)) return _instance;` in the `Instance` property, so it's not optimal if you call `Instance` in a `Update` loop or something similar.

Surely we can do better than this.

### Secure UnitySingleton
[SecureUnitySingleton](http://wiki.unity3d.com/index.php/Secure_UnitySingleton) is the last one of the three singleton implementation in [unity3d](http://wiki.unity3d.com). It has a very clear idea about the usecases of singletons. There are 3 main supported usecases:
* Exists In Scene: Searches the current scene for an object with the singleton component attached to it.
* Loaded From Resources: This type creates an instance of a prefab with the singleton component attached to it from a Resources folder.
* Create on New GameObject: This type creates a new GameObject and attaches a new instance of the singleton component to it.

There are several issues with approach
* Even though the code is quite functional, it still suffers the performance penalty from checking too many things in the `Instance` property.
* Lack of lifecyle methods. Even though it provides a static `DeleteInstance` method, there's no other methods to execute when the instance is created. You might think that `Awake` can be used for that purpose, but it not explicit enough that `Awake` is called immediately after `Instance` is called. Another possible issue is `Awake` will not be called when the prefab is disabled, which should never be desirable but can happen due to a mistake from the developers.

This is quite good but surely we can do better.

## Discussions
First of all, we realize that non of the above methods take into account concurrency issue. If we care about concurrency we can do something like this:

```
    public class MySingleton ...
    {
        static MySingleton _instance = null;
        static object singletonLock = new object ();

        public static MySingleton Instance
        {
            get {
                if (_instance != null) {
                    return;
                }

                lock (singletonLock) {
                    if (_instance != null) {
                        return _instance;
                    }

                    var singletonGameObject = new GameObject ("MySingleton");
                    GameObject.DontDestroyOnLoad (singletonGameObject);
                    _instance = singletonGameObject.AddComponent< MySingleton > ();

                    ... other initialization code
                }

                return _instance;
            }
        }
```

By using a simple double lock pattern, we seemingly solve the "concurrency problem". The question is: Do we need to?. Why you have the concurrency problem with singleton? It's because you want to `lazy load` the singleton, i.e. only create it when it is used for the first time. But that's exactly what we want to avoid if we want to achieve smooth gameplay. So what you should do instead is just create the bloody singleton at the beginning and forget about it. Remember, `preload` is better than `lazy load`.

Secondly, I've already mentioned the check for null is redundant if we know we only call the singleton after it's been initialized. In the usecases listed by `SecureSingleton`, we see that the singleton is either created by code or already exists in the scene as a `GameObject` which is supposed to be configured by designers. In either case, the code to initialize the scene should be a good place for calling the initialization code of the singleton and there's no need for making it sooner.

So what will happen if the `Instance` property is called before you initialize the singleton? Obviously an exception will be thrown and this is an ideal case for using Unity Assert because you will have a nice message in development mode but you can also turn it off in production build.

```
	public class GameSingleton<T> : MyBaseBehaviour where T : GameSingleton<T>
    {
        ...
        public static T Instance
        {
            get {
                Assert.IsNotNull (_instance);
                return _instance;
            }
        }
```

Note that `MyBaseBehaviour` class is a class derived from `MonoBehaviour` and is customized specifically for our game. For instance, it might have general code for handling `Update` or `OnDestroy`.

All that is left now is writing a function `CreateInstance` for creating the singleton. This function should be called once only at the exact place where you want it. This means we should design it in such a way to discourage it from being called multiple times randomly by some careless developers. Calling `CreateInstance` twice should throw an exception. This is better than mindlessly guard the function in the name of "defensive programming". It will look something like this:

```
		public static T CreateInstance()
		{
            Assert.IsNull (_instance);

			GameObject go = new GameObject(typeof(T).Name);
			_instance = go.AddComponent<T>();
			_instance.OnCreated();
			DontDestroyOnLoad(go);

			return _instance;
		}


		protected virtual void OnCreated()
		{
		}
```

Here we have a virtual function `OnCreated` waiting to be overriden in subclass. To destroy the singleton, we don't have to use fancy static function `DeleteInstance`, instead we can just get the singleton gameobject and destroy it like this:

```
    GameObject.Destroy (MySingleton.Instance.gameObject);
```

When the `OnDestroy` function is called, we will do some clean up then call a special function `OnDisposed` to allow subclass do their specific cleanup activities.

