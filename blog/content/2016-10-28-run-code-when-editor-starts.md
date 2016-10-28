Title: Run specific code when Editor starts
Date: 2016-10-28 00:00
Author: Ha.Minh
Category: Unity
Tags: unity

Sometimes we want to execute code whenever we hit `Play` button in Unity Editor. The reason for this usually is that we want to enforce some workflow automatically such as getting specific environment information (e.g. git hash, date) and fill it in a prefab or something. We could do these things by creating a Custom Window with a button somewhere, but it feels too manual.

Fortunately, Unity has offered a simple way to do this, that is `InitializeOnLoadAttribute`. You can check an usecase of it at [http://blog.andreimarks.com/2012/08/16/unity-how-to-run-specific-code-only-when-building-out-a-project/](http://blog.andreimarks.com/2012/08/16/unity-how-to-run-specific-code-only-when-building-out-a-project/). Beware of a potential problem [here](http://www.createdbyx.com/post/2013/02/17/Unity-Tip-101-55-%E2%80%93-InitializeOnLoad-ResourcesLoad-gotcha%E2%80%99s.aspx)

Other ways to execute code on startup are listed here [http://www.codingjargames.com/blog/2015/08/04/unity-and-initialization-order/](http://www.codingjargames.com/blog/2015/08/04/unity-and-initialization-order/)

