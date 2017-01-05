Title: Dither Unity textures to save memory
Date: 2017-01-05 00:00
Author: Ha.Minh
Category: Unity
Tags: unity, dither

The project code is here: https://github.com/minhhh/unity-texture-dither

In many cases, we want to dither textures so that we can use more compact texture import format to save memory. This project aims to provide a workflow for dithering imported texture automatically, based on settings that can be swapped easily. Note that this has nothing to do with using dithering to achieve some artistic goal or the real time dithering effect to solve color banding problem.

The algorithms are explained in a [blog post](http://www.tannerhelland.com/4660/dithering-eleven-algorithms-source-code/) by Tanner Helland and the reference implementations are taken from https://github.com/mcraiha/Dithering-Unity3d with some slight modification.

## Usage

To dither images, put them in a folder whose name ended with `Dither`. Then click on the folder and `Reimport`.

The dither setting, i.e. algorithm and output color space is defined in ScriptableObjects `DitheringAlgorithmSetting`. You can find them in the `Assets` folder. To change dither setting, select `Settings > TextureDitherSetting` and change the field `Dither Algorithm Setting` accordingly.

Supported algorithms are:

* Atkinson
* Burkes
* FloydSteinberg
* JarvisJudiceNinke
* Sierra
* SierraLite
* SierraTwoRow
* Stucki
* No Dithering (for testing purpose)

Supported color spaces are:

* RGBA4444
* Websafe
* TrueColor (for testing purpose)
