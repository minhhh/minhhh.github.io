Title: How to do blur effect in Unity
Date: 2016-11-24 00:00
Author: Ha.Minh
Category: Unity
Tags: unity, blur

**Image Blur**

* can use a camera which render to a rendered texture
* add the images to be rendered to a second canvas, which uses the new camera with screenspace-camera
* Add blur shader to the Camera, or a parent object which contains all images
* Add the rendered texture to anywhere you like in the first camera


**Dynamic Background Blur**

* [Blur Behind Window](http://answers.unity3d.com/questions/21699/unity-blur-behind-window.html) Use Camera post effect
* [Dynamic Blurred Background on UI](http://forum.unity3d.com/threads/solved-dynamic-blurred-background-on-ui.345083/) Use Grabpass
* http://blog.ivank.net/fastest-gaussian-blur.html
