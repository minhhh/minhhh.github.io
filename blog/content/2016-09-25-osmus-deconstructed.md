Title: Osmus Deconstructed
Date: 2016-09-25 00:00
Author: Ha.Minh
Category: Programming
Tags: deconstructed, network

[Osmus](https://github.com/borismus/osmus) is a tech demo of a HTML5 multiplayer game inspired by [Osmos](http://www.osmos-game.com/).

**Deconstruction**

* Osmus uses node.js for the server and HTML5 Canvas with Javascript on the client side. The simulation code is shared between client and server.
* Regarding network, Osmus uses `socket.io`. `Socket.io` is quite stable and performant so this is ok.
* The multiplayer architecture is Server/Client, with the server being the sole authority. All inputs from any client will be rebroadcast to all clients in the room. There are several problems with this approach
    * Not scalable: Simply rebroadcast all messages will increase the load on the server exponentially so this is totally not acceptable. Some sort of rate limit should be applied, such as only sending messages to viewable entities.
    * Sudden positional jump on client: If the client entities can move around, then client simulation. client prediction and interpolation with server states should be applied to ensure smooth movement.
