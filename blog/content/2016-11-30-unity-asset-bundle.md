Title: Unity Asset Bundle
Date: 2016-11-30 00:00
Author: Ha.Minh
Category: Unity
Tags: unity, assetbundle

Asset Bundle is a big topic in Unity. Initially, you want to grasp the basic setup and make something work. As your games get bigger, you might want to do more customization to make sure you have full control of the lifecycle. Here are some documents I've studied while learning about asset bundle. Ultimately, my goal is to make a full asset bundle workflow for big online game, so this blog will be a work in progress until I can transfer it into a working repository.

* Asset bundle and AssetBundleManager
    * [AssetBundles and the AssetBundle Manager](https://unity3d.com/learn/tutorials/topics/scripting/assetbundles-and-assetbundle-manager)
        * AssetBundles are downloaded and cached in their entirety.
        * AssetBundles do not need to be loaded in their entirety.
        * Assets in AssetBundles can have dependencies on other assets.
        * Assets in AssetBundles can share dependencies with other assets.
        * Each AssetBundle has some technical overhead, both in the size of the file and the need to manage that file.
        * AssetBundles should be built for each target platform.
    * The steps of working with AssetBundles in the editor fall roughly into these steps:
        * Organizing & Setting-up AssetBundles in the editor.
        * Building AssetBundles.
        * Uploading AssetBundles to external storage.
        * Downloading AssetBundles at run-time.
        * Loading objects from AssetBundles.
    * Using Asset Variants to support different resolution
        * Create Variants folder
        * Create corresponding SD and HD folder (must be same structure)
    * Pack sprites into AssetBundle
        * Use packing tag normally. Remember to set Sprite Mode: Single. Then set the AssetBundle
    * Load sprite sheet from Asset Bundle
        * Can load Sprite or Texture2D, but it can't load Sprite from a SpriteSheet directly
        * http://forum.unity3d.com/threads/packing-a-texture-sprite-sheet-in-an-asset-bundle-with-already-sliced-subtextures-possible.313186/
        * Basically use LoadAssetWithSubAssets
    * Issues
        * No subfolder inside AssetBundle
        * Clear cache in `~/Library/Caches/Unity/` [http://www.leandro.co.uk/unity/caching-assetbundles-in-unity/](http://www.leandro.co.uk/unity/caching-assetbundles-in-unity/)
        * Loading prefabs with script references from assetbundle
            * http://answers.unity3d.com/questions/1032495/loading-prefabs-with-script-references-from-assetb.html
        * Variants with prefab
            * http://forum.unity3d.com/threads/official-how-did-asset-bundle-variant-fail-to-satisfy-your-hd-sd-use-case.375716/
        * Bundles have to be updated across unity version: http://forum.unity3d.com/threads/end-of-the-resources-folder.363800/
            * Or force player to update their client
            * Client has to update and redownload ALL bundles
<br/>

* [AssetBundle usage patterns](https://unity3d.com/learn/tutorials/topics/best-practices/assetbundle-usage-patterns)
    * If an AssetBundle is unloaded improperly, it can cause Object duplication in memory
    * Most projects should use AssetBundle.Unload(true) and adopt a method to ensure that Objects are not duplicated
    * [AssetBundle.CreateFromMemory](https://unity3d.com/ru/learn/tutorials/topics/best-practices/assetbundle-fundamentals#Loading_Asset_Bundles)
        * loads an AssetBundle from a managed-code byte array (byte[] in C#)
        * If the AssetBundle is LZMA compressed, it will decompress the AssetBundle while copying
        * Uncompressed and LZ4-compressed AssetBundles will be copied verbatim
        * The peak amount of memory consumed by this API will be at least twice the size of the AssetBundle: one copy in native memory created by the API, and one copy in the managed byte array passed to the API
        * Assets loaded from an AssetBundle created via this API will therefore be duplicated three times in memory
    * [AssetBundle.CreateFromFile](https://unity3d.com/ru/learn/tutorials/topics/best-practices/assetbundle-fundamentals#Loading_Asset_Bundles)
        * If the AssetBundles are uncompressed or LZ4
            * On device: only load the AssetBundle's header. Objects are loaded on-demand. No excess memory will be consumed.
            * On Editor: load the entire AssetBundle into memory
        * Calls to AssetBundle.LoadFromFile will always fail for LZMA-compressed AssetBundles.
    * [WWW.LoadFromCacheOrDownload](https://unity3d.com/ru/learn/tutorials/topics/best-practices/assetbundle-fundamentals#Loading_Asset_Bundles)
        * WWW object will keep a full copy of the AssetBundle's bytes in native memory
        * 3 ways to avoid
            * Keep AssetBundles small
            * If using Unity 5.3 or newer, switch to using the new UnityWebRequest API's DownloadHandlerAssetBundle, which does not cause memory spikes during downloads.
            * Write a custom downloader. For more information, see the Custom downloaders section.
            * Write a custom downloader
    * [AssetBundleDownloadHandler](https://unity3d.com/ru/learn/tutorials/topics/best-practices/assetbundle-fundamentals#Loading_Asset_Bundles)
        * LZMA-compressed AssetBundles will be decompressed during download and cached uncompressed.
        * does not keep a native-code copy of all downloaded bytes
        * supports caching in a manner identical to WWW.LoadFromCacheOrDownload
    * Examples of situations which may prevent the use of UnityWebRequest or WWW.LoadFromCacheOrDownload:
        * When fine-grained control over the AssetBundle cache is required
        * When a project needs to implement a custom compression strategy
        * When a project wishes to use platform-specific APIs to satisfy certain requirements, such as the need to stream data while inactive. Example: Using iOS' Background Tasks API to download data while in the background.
        * When AssetBundles must be delivered over SSL on platforms where Unity does not have proper SSL support (such as PC).
    * AssetBundles in the caching system are identified only by their file names
    * LZ4 decompress individual Objects without needing to decompress the entire AssetBundle

<br/>
* [Unity AssetBundle summary](https://matome.naver.jp/odai/2139114084705385001)
    * [Unite Japan 2013] Scene / Memory / Asset Bundle
        * 【process】
            * ① Build the asset bundle (A).
            * ② Download the asset bundle (A).
            * ③ Load the asset bundle (A).
            * ④ Load the asset (B) from the asset bundle.
            * ⑤ Generate an instance (C) of the asset.
            * ⑥ Unload the asset bundle (A).
            * (Note that unloaded assets can not depend on other assets)
            * ⑦ Discard instance (C).
            * ⑧ Unload asset (B).
        * AssetBundle placement place】
            * ① Server
            * ② In the StreemingAsset folder
        * Minimize size of AssetBundle】
            * ① It does not depend on others (Include all referenced assets in AssetBundle.)
            * ② It depends on in-app scripts and basic components.
            * ③ It depends on another AssetBundle.
        * 【Correspondence by Platform】
            * ① Editor (If you are looking at bundled assets bundle, it will be difficult to test, so let's do something.)
            * ② Android
            * ③ IOS
        * 【How to Load Asset Bundle】
            * ① Use the cache. 'WWW.LoadFromCacheOrDownload'
            * (Note: 150 days deletion and caching can not be deleted.)
            * ② One time only "WWW (" http: // ... "), WWW (" file: // ... ")"
            * ③ Save locally and do not use cache. "AssetBundle.CreateFromFile, AssetBundle.CreateFromMemory"
        * Supplement 1: How to summarize asset bundles
            * ① Compressed or uncompressed
            * ② Individual or large quantity
        * Supplement 2
            * ① Individual synchronous load
            * ② Individual asynchronous load
            * ③ bulk synchronous load
        * 【Efficient Build】
            * ① Automation
            * ② Folder structure
            * ③ Adjustment of property at build time · · ·
            * (Side street: property adjustment at asset import)
        * 【Correspondence at the time of version up】 · · · I do not use it so I omit it
            * ① Cash on the URL
            * ② Compatibility
        * 【Others】 · · · I do not use it so I omit it
            * ① To use binary data.
            * ② Include the script in the asset bundle. (It is impossible in IOS, so it is omitted)
