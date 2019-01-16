Title: Autoformat C# code from command line
Date: 2016-09-11 00:00
Author: Ha.Minh
Category: Programming
Tags: c#, cli

We all need a tool to format code automatically according to project's convention. Using an IDE like Visual Studio, Xamarin or MonoDevelop, we can format code easily. However, it's not always convenient to fireup the IDE just for formatting some code, and also having a tool on the command line makes it easier to integrate with other workflows. Therefore, it's great if we have some tool which runs on the command line to auto format our code.

**Requirements**
* Customizable format options
* Format whole directory recursively

The second requirement is relatively easy to implement if we have a tool to format a single file on the commandline because we can just use `find` with some filter to iteratively apply the tool to a bunch of files.

## Solution 1: Astyle
[Artistic Style](http://astyle.sourceforge.net/) is a source code indenter, formatter, and beautifier for the C, C++, C++/CLI, Objective‑C, C# and Java programming languages. We can download and install Astyle rather quickly without any problems on most platforms.

**Installation**
We will use a simple script below to help us install AStyle on Mac OSX. Installation on other platforms can be done in a similar manner

**Usage**
After we have `astyle` available on the command line, applying it for our project is a matter of wrapping everything in a single Make command like so

```
# Supposed our Code is in the Code folder
format:
	find Code -iname "*.cs" -not -path "Code/excludedpath/*" | xargs -n 1 -I {} bash -c "astyle --options=.astylerc \"{}\""
```

Remember to create a file called `.astylerc` and put whatever format options you want to customize for your project there.

## Solution 2: NRefactory
[NRefactory](https://github.com/icsharpcode/NRefactory) is the C# analysis library used in the SharpDevelop and MonoDevelop IDEs. We can write a command line client with our customized parameters and format options, which uses `NRefactory` internally to format code.

TODO: Write a cli using `docopt`



