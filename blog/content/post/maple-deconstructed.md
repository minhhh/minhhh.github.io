+++
title = "Maple.js Deconstructed"
date = "2016-09-25T00:00:00+07:00"
author = "Ha.Minh"
categories = ["Programming"]
tags = ["deconstructed", "network"]
+++

[Maple.js](https://github.com/BonsaiDen/Maple.js) is a simple event-based multiplayer framework using Node.js

**Deconstruction**

* Maple provides a base class for `Client` and `Server`. Your specific game code should inherit these base classes.
* The supported functionality includes:
    * Connect/Disconnect
    * Ping server
    * Handle arbitrary message
    * Sync client server update tick on every frame
* The problems with Maple are:
    * Use Websocket, which is slow
    * Require too much sync and only applicable for Round-based games.
