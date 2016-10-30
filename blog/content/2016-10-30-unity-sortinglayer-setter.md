Title: Setting sorting layer and order in layer of Mesh Renderer
Date: 2016-10-30 00:00
Author: Ha.Minh
Category: Unity
Tags: unity

Unity 5.x exposes the sorting layer and order in layer of `SpriterRenderer`, but not `MeshRenderer`. Fortunately, it's very easy setting these property of the `MeshRenderer` in code. I've created a simple solution for setting sorting layer and order in layer of any `Renderer` component using a simple component called [SortingLayerSetter](https://github.com/minhhh/unity-sortinglayer-setter).

It looks like this in the Editor

[example 1](https://github.com/minhhh/unity-sortinglayer-setter/blob/master/images/example1.png)
