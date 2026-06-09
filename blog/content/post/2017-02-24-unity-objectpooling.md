+++
title = "Unity Object Pooling"
date = "2017-02-24T00:00:00+07:00"
author = "Ha.Minh"
slug = "unity-objectpooling"
categories = ["Programming"]
tags = ["unity", "pool"]
+++

An object pool provides an efficient way to reuse objects, and thus keep the memory foot print of all dynamically created objects within fixed bounds. This is crucial for maintianing consistent framerates in realtime games (especially on mobile), as frequent garbage collection spikes would likley lead to inconsistent performance.

Implementing object pool is quite straight forward. There are several open-source solutions already so don't bother looking into AssetStore.

* [Leanpool](https://github.com/minhhh/unity-leanpool)
* [Unity Object Pool](https://github.com/thefuntastic/unity-object-pool)
* [RecyclerKit](https://github.com/prime31/RecyclerKit)
