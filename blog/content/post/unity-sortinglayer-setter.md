+++
title = "Setting sorting layer and order in layer of Mesh Renderer"
date = "2016-10-30T00:00:00+07:00"
author = "Ha.Minh"
categories = ["Unity"]
tags = ["unity"]
+++

Unity 5.x exposes the sorting layer and order in layer of `SpriterRenderer`, but not `MeshRenderer`. Fortunately, it's very easy setting these property of the `MeshRenderer` in code. I've created a simple solution for setting sorting layer and order in layer of any `Renderer` component using a simple component called [SortingLayerSetter](https://github.com/minhhh/unity-sortinglayer-setter).

It looks like this in the Editor

![example 1](https://raw.githubusercontent.com/minhhh/unity-sortinglayer-setter/master/images/example1.png)
