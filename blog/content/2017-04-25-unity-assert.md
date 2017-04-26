Title: Using Unity Assert
Date: 2017-04-25 00:00
Author: Ha.Minh
Category: Unity
Tags: unity, assert

Even though Unity's [UnityEngine.Assertions](http://blog.theknightsofunity.com/unity-5-1-assertion-library/) is great, it has two major disadvantages

* We cannot extend it
* It does not have the concept of error code. Using error code, we can force developers to explicitly think about how they will categorize the error so it's easier to analyze the error when the game crashes

Therefore I put together a simple script to do assertion here: [https://github.com/minhhh/UBootstrap.Assert](https://github.com/minhhh/UBootstrap.Assert)

Our `CUSTOM_ASSERT` class provides the almost the same interface as `UnityEngine.Assertions.Assert`:

* `IsTrue (bool condition, int errorCode, string message = "", params object[] args)` - Asserts that the condition is true.
* `IsFalse (bool condition, int errorCode, string message = "", params object[] args)` - Assert that condition is false
* `IsNull (object value, int errorCode, string message = "", params object[] args)` - Assert that value is null.
* `IsNotNull (object value, int errorCode, string message = "", params object[] args)` - Assert that value is not null.
* `AreEqual<T> (T expected, T actual, int errorCode, string message = "", params object[] args)` - Assert that the values are equal.
* `AreNotEqual<T> (T expected, T actual, int errorCode, string message = "", params object[] args)` - Assert that the values are not equal.
* `AreApproximatelyEqual (float expected, float actual, int errorCode, float tolerance, string message = "", params object[] args)` - Asserts that the values are approximately equal. An absolute error check is used for approximate equality check (|a-b| < tolerance). Default tolerance is 0.00001f.
* `AreNotApproximatelyEqual (float expected, float actual, int errorCode, float tolerance, string message = "", params object[] args)` - Asserts that the values are approximately not equal. An absolute error check is used for approximate equality check (|a-b| < tolerance). Default tolerance is 0.00001f.
* `Fail (int errorCode, string message = "", params object[] args)` - Just fail the assertion.

The reason it's named `CUSTOM_ASSERT` is to make it look like a macro definition. In fact, you have to define a macro named `CUSTOM_ASSERT` to include it in your build, similarly to the macro `UNITY_ASSERTIONS` from Unity.

`CUSTOM_ASSERT` class is defined as a partial class. It is expected that you define your part of the partial class, so that you can provide some default error code for common functions. You can find an example in `Assets/MY_ASSERT.cs`. It is also recommended that you define your own sets of error codes.

There is no way to include the assertion without throwing exception, because it does not make sense to assert something that does not crash the build if its not true. Those set of errors belong to a logger, not an assert utility.
