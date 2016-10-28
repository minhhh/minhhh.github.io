Title: MVC in Unity
Date: 2016-10-27 00:00
Author: Ha.Minh
Category: Unity
Tags: unity, mvc

# Some MVC like frameworks in Unity

**[Karma](https://github.com/cgarciae/karma)** Lightweight MVC framework using Zenject DI container. It is inspired from [MODEL VIEW CONTROLLER PATTERN FOR UNITY3D USER INTERFACES](http://engineering.socialpoint.es/MVC-pattern-unity3d-ui.html)

**[Marklight](https://www.assetstore.unity3d.com/en/#!/content/37466)** Looks nice. It offers XUML and external editor which might be good for view management, but it also feels too restrictive because you have to follow their way.

**[Unity3d.UI.Windows](http://chromealex.github.io/Unity3d.UI.Windows/)** Uses a Window system to create UI and layout elements. Try doing too many things: Audio, Tweening

**[strangeioc](https://github.com/strangeioc/strangeioc)** Obsolete and not maintained

**[uFrame MVVM](https://www.assetstore.unity3d.com/en/#!/content/14381)** It's trying to do too much by offering a graphing/diagramming engine and code generation. I really don't like code generation

# Discussion

It looks like the main advantages of using these MVC frameworks are:

* Some of them can support theme change
* They have some existing controls so you don't have to implement yourself.

However, there are several disadvantages:

* If you don't need to change theme then definitely you don't need to separate View and ViewModel or Presenter.
* UI usually consists of a big container and a lot of smaller views. Testing small views is easy so you don't need to create separate View class for each. Testing the container is complicated, you want to do it with a test scene in Unity anyway, thus there's no need to try to make an ViewModel interface for testing.
* The examples of Unity MVC implementation in some blogs are usually naive and contrived. As such, they don't scale when you have really complex UI. In addition, they usually confuse between UI and gameplay, so they take example such as hitting enemies or updating their HP bar. MVC is suitable for UIs and maybe some turn-based gameplay, but extending it to a fighting gameplay requires much more than some optimistic guesswork.
* Controller needs to behave according to states, that makes the ViewPresenter or ViewModel also have to replicate those states fully or partly. It's quite difficult to know which should be the common behaviour. A simpler way is to just merge Controller and View/ViewPresenter/ViewModel.

