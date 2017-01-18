Title: Using Webp texture format in Unity
Date: 2017-01-18 00:00
Author: Ha.Minh
Category: Unity
Tags: unity, texture, webp

Webp is a very optimized image format. It will produce smaller image size with almost the same quality as other compression format such as: `ETC2`, `DXT5`, `ETC1`, `PVRTC`. Below is some comparison between `Webp` and popular compression format in Unity

| 512x512 Image | Size in KB     |
| ------------- | -------------: |
| Original      | 480            |
| ETC1 4bits    | 128            |
| ETC2 8bits    | 256            |
| Dxt5 Crunched | 64             |
| PVRTC 2 bit   | 64             |
| PVRTC 4 bit   | 128            |
| Webp Lossless | 287            |
| Webp Lossy 80 | 23             |


| 1024x1024 Image | Size in KB     |
| -------------   | -------------: |
| Original        | 1800           |
| ETC1 4bits      | 512            |
| ETC2 8bits      | 1000           |
| Dxt5 Crunched   | 183            |
| PVRTC 2 bit     | 256            |
| PVRTC 4 bit     | 512            |
| Webp Lossless   | 1200           |
| Webp Lossy 80   | 113            |

I've written a simple plugin to include Webp textures into your Unity game here: https://github.com/minhhh/UBootstrap.Webp

Ref: [png vs webp](https://www.andrewmunsell.com/blog/png-vs-webp/)
