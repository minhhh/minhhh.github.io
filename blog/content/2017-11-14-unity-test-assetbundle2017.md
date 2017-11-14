Title: Test AssetBundle in Unity 2017
Date: 2017-11-14 00:00
Author: Ha.Minh
Category: Unity
Tags: unity, assetbundle

With Unity 2017, we can use 2 tools to build Asset Bundle: [AssetBundles-Browser](https://github.com/Unity-Technologies/AssetBundles-Browser) and [AssetGraph](https://github.com/unity3d-jp/AssetGraph). I've created a test project [here](https://github.com/minhhh/unity-test2017-assetbundle)

## General flow
1. Setup `Asset Bundle Graph` to build AssetBundles
2. Check AssetBundles with AssetBundleBrowser


**Setup Asset Bundle Graph**

The most basic setup consists of 4 nodes:

1. Load From Directory
2. Group By File Path
3. Configure Bundle From Group
4. Build Asset Bundles

In step 1, we create a folder that represents all resources related to an entity in our system, this could be a character or an enemy NPC. In step 2 we want to create one AssetBundle for each of the sub-folders in the parent folder. Each AssetBundle represents an aspect of the entity, such as by resource types: textures, materials, animations, or by enemy types: fast, slow. Step 3 applies naming convention to the AssetBundle's name. Step 4 is obvious, building the final asset bundles.

There are 2 examples of Asset Bundle Graph (ABG) in `Assets/Tests`: `ABG_with_regex` and `ABG_with_wildcard`.

In the `ABG_with_regex` example, we used the pattern `/Missile\/(.*)/`. There are several issues with this approach:

1. It's not real regex since we cannot use `(.+)` and we are forced to use `(.*)`.
2. It creates group for sub-sub-folder. For example, it creates a group named `Object/Materials` instead of just putting it inside group `Object`
3. The main blocker issue is the error `Moving file failed` when building AssetBundles

In the `ABG_with_wildcard` example, the group is created correctly for each of the sub-folders. There is still some issues:

1. We cannot have `.` in the group name because if we do then the part after `.` will be considered variant.
2. We cannot have variants of sub-folder, we have to use the folder name itself as variant

This is just a rough test and obviously we require much more for an usable workflow.
