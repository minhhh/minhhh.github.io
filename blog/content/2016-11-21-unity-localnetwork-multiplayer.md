Title: Unity local network multiplayer
Date: 2016-11-21 00:00
Author: Ha.Minh
Category: Unity
Tags: unity, bluetooth, multiplayer

iOS device can connect to iOS device via Bluetooth using:

* [MultiPeer Local Multiplayer Plugin](https://www.assetstore.unity3d.com/en/#!/content/2739)
* [GameCenter Multiplayer plugin](https://prime31.com/docs#iosGCMP)
* U3DXT


Android device can connect to Android device via Bluetooth using:

* Android Bluetooth Multiplayer (Pro)


[https://github.com/DarkRay/Unity3D-bluetooth](https://github.com/DarkRay/Unity3D-bluetooth) A low level bluetooth library.


Android and iOS cannot connect to each other via iOS as mentioned [here](http://stackoverflow.com/questions/18884705/transfer-data-between-ios-and-android-via-bluetooth).

[Unity3D for iOS and Android: Multiplayer](http://stackoverflow.com/questions/13032540/unity3d-for-ios-and-android-multiplayer-bluetooth-connection). Options for multiplayer game

* via Bluetooth (using Prime31 plugin)
    * iOS
* via LAN (using Unity RPC) The players can start combats in a Local Area Network with any of above devices: iOS vs iOS, iOS vs Android, Android vs Mac, and so on.
    * iOS
    * Android
    * Mac
    * Web (Kongregate)
* via Game Center (using Prime31 plugin): Uses the Game Center multiplayer to match combats.
    * iOS
* via Global Server (an in-house solution): The players can start combats around the world with any of above devices: iOS vs iOS, iOS vs Android, Android vs Mac, and so on.
    * iOS
    * Android
    * Mac
    * Web (Kongregate)

[UNET](https://docs.unity3d.com/Manual/UNetOverview.html) the new Unity Networking library.

* [Unet sample projects](https://forum.unity3d.com/threads/unet-sample-projects.331978/)
* [Multiplayer Networking Tutorial](https://unity3d.com/learn/tutorials/topics/multiplayer-networking/introduction-simple-multiplayer-example?playlist=29690)
* [Unity 5 UNET Multiplayer Tutorials](https://forum.unity3d.com/threads/unity-5-unet-multiplayer-tutorials-making-a-basic-survival-co-op.325692/)


[TNET](http://www.tasharen.com/?page_id=4518) Another option which uses UDP for multiplayer game.

[Alljoyn](https://allseenalliance.org/framework) makes it easy for devices to communicate. Unfortunately it does not support Unity.

