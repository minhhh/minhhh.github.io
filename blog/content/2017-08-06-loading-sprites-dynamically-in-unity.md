Title: Loading Sprites dynamically in Unity
Date: 2017-08-06 00:00
Author: Ha.Minh
Category: Unity
Tags: unity

Loading sprites dynamically from code is one of the most basic tasks that we have to do. However, it seems that there's not a standard way to to this in Unity. This guide will look at several cases of loading sprites dynamically and their solutions

**Loading a separate sprite**

Imagine you have 4 attribute icons: fire, water, earth and wind. You will have to load the correct icon for the correct character. The easiest way to do this is to put 4 icon images: fire.png, water.png, earth.png and wind.png inside a folder in `Resources`, such as `Resources/attribute_icons/`. Then loading a sprite is as simple as this:

```
Sprite sprite = Resources.Load ("attribute_icons/fire", typeof(Sprite)) as Sprite;
```

In reality, we almost never do this. The reason is we need to batch drawcall, so we cannot afford to have separate drawcall for each of these small icon images. But if you put the sprites inside the `Resources` folder, you cannot pack them with Unity's Sprite Packer. If you put them outside of the `Resources` folder, you cannot load them dynamically with Resources.Load. This leads to the next solutions.

**Packing spritesheet with external tools**

Unity has a Sprite import mode called `Multiple`, where you can slice a Sprite atlas or Spritesheet into multiple sprites. The sprites can then be load dynamically like this:

```
// suppose the texturesheet is in Resources/attributeicons.png
Sprite[] sprites = Resources.LoadAll <Sprite> ("attributeicons");
// Find the correct sprite to use by Sprite.name
```

Obviously, you would not want to create the Sprite atlas and slice sprites by hand in a real game (not a tutorial). Therefore, you will use an external tools to create the Sprite atlas. There are several solutions:

1. Write your own texture packer (or use an existing one you can easily find in github). Remember to export the UVs information to text, or json and copy it to Unity. In Unity, you have to write an Editor extension to slice the Sprite atlas using the Uvs information in the text/json file. I have a tool and Unity code for this but I cannot publish them due to copyright. They're super easy to create though.
2. Use a full solution inside Unity. You will have the original textures in Unity, then the Sprite atlas will be created inside Unity easily by dragging, dropping sprites to the tools, or some other similar method. You can try the asset [SimpleSpritePacker](https://www.assetstore.unity3d.com/en/#!/content/23276).
3. Use [TexturePacker](https://www.codeandweb.com/texturepacker). This is the best solution since it creates much more optimized sprites. But it costs 40 dollars.

**Packing sprites using Unity Sprite Packer**

One big disadvantage with using  external tools is that you cannot move sprites easily. If you move a sprite from one path to another, you will have to update the path in all objects that use that sprite. Using Unity sprite packer, you can do it like so:

1. Mark a Sprite with a packing tag
2. Use the sprite in a GameObject or Prefab freely
3. A spritesheet will be created by Unity automatically. The sprite will be loaded automatically from that sprite sheet.

So this is perfect, but you cannot load sprite dynamically anymore? There're 2 solution for this problem.

First, you can add all the needed sprites to whatever objects using them, then enable/disable the correct ones by code. This solution works for small projects but it does not scale.

The second solution is to use a tool that automatically load all the sprites into a prefab that can be loaded dynamically in runtime. A sample of this solution is https://github.com/minhhh/UBootstrap.SpriteCollection

![Spritecollection example](https://raw.githubusercontent.com/minhhh/UBootstrap.SpriteCollection/master/imgs/img1.png)



