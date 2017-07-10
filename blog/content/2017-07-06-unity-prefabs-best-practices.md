Title: Unity Prefab Best Practices
Date: 2017-07-06 00:00
Author: Ha.Minh
Category: Unity
Tags: unity, prefab

**Link prefabs to prefabs; do not link instances to instances** This is from [50 Tips for Working with Unity](http://devmag.org.za/2012/07/12/50-tips-for-working-with-unity-best-practices/)

**Use GameObject.Find to establish links between instances** if you have to. It's best to not having to establish links between instances and use prebabs instead. **Don't** link instance to instance like this article suggests (https://akbiggs.silvrback.com/please-stop-using-gameobject-find)

**Apart from UI component, refrain from using GameObject.Find** because there are many better alternatives such as using interfaces, dependency injection, design patterns and so on.


**Remove prefab links from scene object** (https://github.com/minhhh/unity-tips/blob/master/README.md#tips-using-editors)


## References
* [50 Tips for Working with Unity](http://devmag.org.za/2012/07/12/50-tips-for-working-with-unity-best-practices/)
* [Unity Devs, stop using GameObject.Find!](https://akbiggs.silvrback.com/please-stop-using-gameobject-find)
