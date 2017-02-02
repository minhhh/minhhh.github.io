Title: Better Unity workflow with command line
Date: 2017-02-02 00:00
Author: Ha.Minh
Category: Unity
Tags: unity, commandline

To do certain tasks for our game workflow, we will need to use other external tools that can only called from the command line. One way to do this is to switch back and forth between Unity and the command line, obviously this is not the best way. Our goal is to use only 1 click, or one action to execute a series of tasks in Unity and in the command line.

There are 2 ways to achieve this:

* Create an editor script and call the command line, along with other Editor scripts. This is good if you want to stay in Unity all the time.
* Create a command line script that call other command line scripts and some Unity scripts. This is good for continuous integration.

To launch Unity from the command line, look at these references:

* [Making most of Unity's command line](https://effectiveunity.com/articles/making-most-of-unitys-command-line.html)
* [Command line arguments](https://docs.unity3d.com/Manual/CommandLineArguments.html)

To run command line scripts from Unity, look at these references:

* [Running command line action through C# script](https://web.archive.org/web/20170202150301/https://effectiveunity.com/articles/making-most-of-unitys-command-line.html)
