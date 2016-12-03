Title: Unity Texture compression and optimization
Date: 2016-12-03 00:01
Author: Ha.Minh
Category: Unity
Tags: unity, texture, splitalpha, optimization

A common question when building Unity games is which texture compression format will be the best. The criteria are: size on disk, memory footprint, performance.

We have many options in the Unity Engine: ETC1, ETC2, DXT3, DXT5, and so on. How do we choose? Let's look at some optimization tricks to see how others choose their formats.

First you need to understand [How much memory does a texture take up on the GPU?](http://gamedev.stackexchange.com/questions/5171/how-much-memory-does-a-texture-take-up-on-the-gpu)

* many modern engines opt to store the same format on disk as they do in memory, leading to files that are the same size as the texture's memory requirements
* Uncompresed image of 256x256 is 256KB. A DXT1 image of 256x256 is 32KB. And DXT3 or DXT5 is 64KB
* [http://mainroach.blogspot.com/2014/03/the-png-vs-gpu-battle-on-android.html](http://mainroach.blogspot.com/2014/03/the-png-vs-gpu-battle-on-android.html) also explains why you don't want to use plain `png` textures. Instead, export them to `DXT1`, `PVR` or `ETC`

[Efficient Game Textures with Hardware Compression](https://web.archive.org/web/20160826092252/http://android-developers.blogspot.com/2015/01/efficient-game-textures-with-hardware.html) examines preferable compression formats which are supported on the GPU to help you reduce .apk size and loading times of your game:

* As you can see, with higher OpenGL support you gain access to better formats. There are proprietary formats to replace ETC1, delivering higher quality and alpha channel support. These are shown in the following table:
    * ATC	Available with Adreno GPU.
    * PVRTC	Available with a PowerVR GPU.
    * DXT1	S3 DXT1 texture compression. Supported on devices running Nvidia Tegra platform.
    * S3TC	S3 texture compression, nonspecific to DXT variant. Supported on devices running Nvidia Tegra platform.
* Using hardware accelerated textures in your games will help you reduce the size of your .apk, runtime memory use as well as loading times.

[Unity 2D Texture Optimization](https://web.archive.org/web/20160507141202/http://biobeasts.artix.com/unity-2d-texture-optimization/) explains how they group textures by type instead of logical groups to save memory:

* 2048x2048 sprite sheet above, even with compression applied, took up 4mb in Texture2D memory
* assets fail to render and appear like black shapes
* organize sprite sheets into three compression types: Solids, Fades, and Alpha Punchouts.
* Solids are any rectangular assets with NO alpha. Here we can get a major savings by selecting a 4-bit compression that doesn't support alpha.
* Alpha Punchouts are any other shapes that use binary alpha, meaning the area of the image is either 100% or 0% alpha. Here we select a 5-bit compression
* Fades are reserved for our most complex objects that contain variable degrees of alpha. We use these sparingly and compress them using a minimum of 8-bit RGBA to look best.

[ETC1 vs ETC2 vs DXT5](https://web.archive.org/web/20160513225925/http://forum.unity3d.com/threads/etc1-vs-etc2-texture-compression.219842/) discuss which is the best texture format

* ETC2 only for devices supporting ES 3.0
* But if your targeting all devices... which u should consider doing in 2015, then it doesnt matter if you pick ETC2 or DXT5 Crunched because theyre both getting decompressed. Which makes sense for ARGB. And then for RGB just ETC1
* Most devices support ETC1 [http://developer.android.com/guide/topics/graphics/opengl.html#textures](http://developer.android.com/guide/topics/graphics/opengl.html#textures)
* I was able to remove 25% of my file size this weekend, thanks to switching to ETC1 + DXT5 Crunched


[Android Texture Compression - a comparison study with code sample](https://web.archive.org/web/20150610061237/https://software.intel.com/en-us/articles/android-texture-compression-a-comparison-study-with-code-sample) compares the quality and sizes of different formats on Android devices including: `png, etc, etc2, pvrtc and s3tc`.

[ETC2 as default texture compression on Android](https://web.archive.org/web/20160513225136/http://forum.unity3d.com/threads/etc2-as-default-texture-compression-on-android.348582/) discuss usage of ETC2 format

* We use DXT5 on our sprites to save space on apk file. When the device does not support your texture type, Unity uses software decompression on load and your textures become 32bit RGBA.
* Use ETC2 to save memory. It might be bad for some low-spec device if they don't support ETC2. Also one more reason to pack your own sheets instead of using Unity packer, since you can do dithering yourself

Some texture optimization recommendations

* Don't use mipmap for 2D [Is it possible to turn on Mip Maps for a sprite](https://web.archive.org/web/20160422114629/http://forum.unity3d.com/threads/is-it-possible-to-turn-on-mip-maps-for-a-sprite.219054/)
* Compress your textures to DXT1 or DXT5 [Memory optimization tricks](https://web.archive.org/web/20160428065248/http://forum.unity3d.com/threads/tips-and-tricks-make-sure-to-profile-your-phone-apps-memory-usage.202952/)
* [What Resolution should I be painting sprites in?](https://web.archive.org/web/20160520084556/http://forum.unity3d.com/threads/what-resolution-should-i-be-painting-sprites-in.225845/) 2048x2048 seems a bit big already on mobile device


[How Can I Add Alpha To ETC1 Compression?](https://support.unity3d.com/hc/en-us/articles/207051116-How-can-I-add-Alpha-to-ETC1-Compression-) attempts to answer the question about ETC1 + Alpha channel

* Sprites placed on some atlas by specifying them with a packing tag
* Make sure to mark the Override for Android checkbox as well as the Compress using ETC1 checkbox. Unity will split the resulting atlas into two textures, each without Alpha and then combine them in the final parts of the RenderPipeline.
* The UI shaders in Unity 5.3.0 and earlier do not support ETC1 + Alpha
* Yes. The UI elements do not work well with ETC1. We have a bug on it. (http://forum.unity3d.com/threads/etc1-alpha-feature.350184/)


[Unity mobile Splitalpha](https://web.archive.org/web/20160726041743/http://developers.mobage.jp/blog/texture-compression). This blogs has solved the issue with ETC1 + Alpha and provided a solution for both Android and iOS devices.

* ETC1 with Alpha channel splitalpha
    * Split Alpha texture

```
                        合計サイズ (MiB) RGBA       16bit 比のサイズ削減率 (%)
RGBA 16bit	            879	                        0
RGBA PVRTC 4bit	        229	                        74
RGBA ETC2 8bit	        431	                        51
Split Alpha (Android)	249	                        72
Split Alpha (iOS)	    272	                        69
```

* https://github.com/keijiro/unity-alphamask

In conclusion, use ETC + Alpha channel whenever you can because it provides the best build size and memory footprint in most cases, at reasonable quality.
