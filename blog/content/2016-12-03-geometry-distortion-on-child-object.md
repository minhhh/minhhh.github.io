Title: Unity geometry distortion on child object
Date: 2016-12-03 00:00
Author: Ha.Minh
Category: Unity
Tags: unity

In Unity there is a geometry issue with the child object of non-uniformly scaled parent. When the parent object does not have (1,1,1) scale, then the child object will be skewed weirdly when they rotate. This issue has been mentioned in the below references:

* http://answers.unity3d.com/questions/197739/object-skewing-on-rotation.html
* http://answers.unity3d.com/questions/21645/geometry-distortion-on-child-objects.html

The solution is to:

1. Make the parent uniform, OR
2. Child the objects to another uniformly scaled parent
