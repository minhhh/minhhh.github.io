+++
title = "Embed git file to pelican"
date = "2014-09-11T00:00:00+07:00"
author = "Ha.Minh"
categories = ["Blog"]
tags = ["git", "pelican", "github"]
description = "Embed git file content into pelican blog"
+++

Writing articles in github pages is nice, because you have github repository with all the nice features for document management, however sometimes it's not where I want my articles to reside. For instance, I want the articles about git to be in a separate `git` repository.

I have several solutions for this problem:

* I could duplicate the article. But I won't do this.
* I could store the articles as `gist` like this:

[gist:id=dc8b7c536d0fe9c7003f]

But I can't store a lot of related things in gist because that's the role of a real git repo.

* I could store the articles in the normal `git` repo, and embed it into the article in github page. I chose this approach for long articles. Like this:

<!-- <script src="http://gistit-minhhh.appspot.com/github/robertkrimen/gist-it-example/blob/master/example.js"></script> -->

There's already a nice tool to do this: [gist-it](https://github.com/minhhh/gist-it). Using it is really simple, just clone the repo and deploy it to an AppEngine instance. The downside of this is it does not generate `html` code for `Markdown`.

* The best solution for me is to use a plugin for embedding git file into `pelican` like this:

[minhhh/wiki/sample.md](https://github.com/minhhh/wiki)
