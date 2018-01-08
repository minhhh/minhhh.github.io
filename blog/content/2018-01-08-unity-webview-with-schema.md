Title: Webview with cchema
Date: 2018-01-08 00:00
Author: Ha.Minh
Category: Unity
Tags: unity

The [unity-webview](https://github.com/gree/unity-webview) plugin is nice, but one thing is you have to call `Unity.call` from Javascript. This is not very convenient for those who design the HTML to quickly assign action related to Unity in hyperlinks.

So I added support for calling Unity function using normal links in HTML using the schema `unity://`. For example, we can put the link: `unity://scene?param1=value1&param2=value2`. When clicking this link, the string `scene?param1=value1&param2=value2` will be passed to Unity, then we can use `WebViewHelper` to parse it furthur into `scene`, `param`, `value1`, `param2`, `value2` and so on.

