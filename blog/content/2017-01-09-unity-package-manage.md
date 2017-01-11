Title: Unity package management
Date: 2017-01-09 00:00
Author: Ha.Minh
Category: Unity
Tags: unity

A robust package management system is quite important when developing in Unity. People have been asking for one in the Unity [forum](https://forum.unity3d.com/threads/any-robust-package-dependency-management-systems-for-unity.276329/). The following survey will list some popular options.

[Projeny](https://github.com/modesttree/Projeny) The purpose of Projeny is to allow your Unity3D project to easily scale in size without heavily impacting development time. Only available in Windows

* Share any Unity assets (code, scenes, prefabs, etc.) across multiple different Unity projects without copy and pasting
* Instantly switch between platforms
* Easily upgrade or downgrade installed asset store packages
* Optimize compile time of your project by getting Unity to only recompile the code that changes most often
* Split up your project into discrete packages, so that you can manage the dependencies between each, instead of having one giant Unity project of inter-related files
* Declare dependencies between packages, so that you always get the packages that you need without needing to hunt down missing libraries or broken links
* Generate a more intelligent Visual Studio solution than the Unity default, using package dependencies to create csproj dependencies

<br/>

[NPM can be used to manage packages and their dependencies](https://github.com/shadowmint/unity-package-template/blob/master/docs/npm.md)

* It's very easy to use and install.
* Can be used with private repo
* Cannot distribute `.unitypackage` file
* However, without using private registry, it cannot force resolve to the latest versions of all dependencies. This issue can be resolved using `yarn install --flat`

<br/>

Some people suggests [using NuGet](http://mymobiledevelopment.blogspot.com/2015/03/unity3d-package-manager.html)

* Seems can download packages correctly
* Have to install a central server to make it work

<br/>

[Paket.Unity3D](http://wooga.github.io/Paket.Unity3D/)

* Same problem as nuget
* Seems to work better in Windows

<br/>

[Unity Kaizen](https://github.com/Unity-Technologies/kaizen)

* Deliver packages via a central repository and zip
* Require more work from package maintainer

<br/>

[UPM](https://bitbucket.org/Zeroto/upm)

* UPM is a package manager designed to work with the Unity game engine. It allows rapid install of unity extension and assets using a command line interface. Packages support dependencies, which will be auto-downloaded when installing a package.
* Seems to be unmaintained
* No MacOS binary


[unity-packman](https://github.com/appetizermonster/unity-packman)

* A command-line client to manage Unity package
* Does not support version and nested versions
* Can only export 1 directory, which is really limited
