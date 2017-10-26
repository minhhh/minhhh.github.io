Title: Unity plugin USplitAlpha
Date: 2017-10-26 00:00
Author: Ha.Minh
Category: Unity
Tags: unity

Last time I discussed about Unity texture compression I've mentioned that using `ETC1` + Alpha channel is the best format because it provides the best build size and memory footprint in most cases. However, Unity does not support split alpha channel for iOS. Recently I had sometime to revisit this and wrote a simple plugin to support split alpha channel on both Android and iOS devices. The plugin is called [USplitAlpha](https://github.com/minhhh/USplitAlpha).

Apparently, the split alpha mechanism is very straightforward so different team will have different workflows that suit them best. For reference, there are some other solutions on github:

* [https://github.com/DragonBones/DragonBoneToUnity/blob/2609886dff00bb503c1795a01aeda7481e28cbd3/Assets/Demo/_Script/Editor/SplitAlpha.cs](https://github.com/DragonBones/DragonBoneToUnity/blob/2609886dff00bb503c1795a01aeda7481e28cbd3/Assets/Demo/_Script/Editor/SplitAlpha.cs)
* [https://github.com/TalosGame/BetterFramework/blob/3eda3261ccc582041aa5e3eaced9089dd4440f75/Assets/Editor/Compression/TextureCompression.cs](https://github.com/TalosGame/BetterFramework/blob/3eda3261ccc582041aa5e3eaced9089dd4440f75/Assets/Editor/Compression/TextureCompression.cs)
* [https://github.com/WakakaYixixi/Unity_extension/blob/c0ba7936f96e0da77a4138249275fc1d89cdebed/Assets/Utils/Editor/SplitAlpha.cs](https://github.com/WakakaYixixi/Unity_extension/blob/c0ba7936f96e0da77a4138249275fc1d89cdebed/Assets/Utils/Editor/SplitAlpha.cs)
