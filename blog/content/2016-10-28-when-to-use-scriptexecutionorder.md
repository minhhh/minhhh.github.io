Title: When to use Script Execution Order
Date: 2016-10-28 00:01
Author: Ha.Minh
Category: Unity
Tags: unity

Normally we don't control the execution order of MonoBehaviour scripts, and we should not. However, there are cases where we do want some scripts to be executed before others. Some usecases include:

1. A Controller script that should be executed as the entry point to the scene
1. Scripts which use `LateUpdate` and must be executed in specific order

For these cases, we will assign an integer number to those scripts in `Edit > Project Settings > Script Execution Order`. It's best practice to use large and discrete number such as `100`, `200`, `-100` instead of `1`, `2`, `3` because it would make it easier to insert something in between them when we need to.

One inconvenience with Unity Editor GUI for Script Execution Order is that it's a bit hard to find your classes when there are a lot of them. The solution for this is to add Script Execution Order as meta information to the class using attribute. There's already an implementation for this: https://github.com/kwnetzwelt/ugb-source/blob/UGB-3.0/UnityGameBase/Core/Editor/GameScriptExecutionOrder.cs and https://github.com/kwnetzwelt/ugb-source/blob/UGB-3.0/UnityGameBase/ScriptExecutionOrderAttribute.cs. Using these 2 classes, now we can add Script Execution Order to any class as follows:

```
    [ScriptExecutionOrder(-1000)]
    public abstract class Game : MonoBehaviour
```
