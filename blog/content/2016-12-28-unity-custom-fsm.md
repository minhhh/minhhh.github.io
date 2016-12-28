Title: Finite state machine for Unity
Date: 2016-12-28 00:00
Author: Ha.Minh
Category: Unity
Tags: unity, editor

Finite State Machine (FSM) is an important technique in game programming. Most games that have some sort of battle will have to design an FSM for its entities. FSM can be applied in UI as well. For example, instead of using flags to enable/disable certain UI elements, we can use a full FSM for all possible states of the targetted UI and its interactions with user inputs.

The main elements of a FSM include:

* A representation of a state
* A representation of a transition between 2 state
* A central system that hosts the states and facilitates their transitions

[Using Interfaces to Make a State Machine for AI](https://unity3d.com/learn/tutorials/topics/scripting/using-interfaces-make-state-machine-ai) has a simplest implementation of FSM. A state is represented like this:

```
public interface IEnemyState
{
    void UpdateState();
    void OnTriggerEnter (Collider other);
    void ToPatrolState();
    void ToAlertState();
    void ToChaseState();
}
```

This implementation hardcodes all state transitions in the interface, thus it's a bad example and should not be used in a serious game.

[A simple finite state machine with C# delegates in Unity](http://www.voidinspace.com/2013/05/a-simple-finite-state-machine-with-c-delegates-in-unity/) provides a slightly better implementation. Instead of hardcoding, it calls a single delegate function when making a transition. Still, it does not separate actions to be executed upon entering and exiting states, so it's not very useful for serious purpose.

[Finite State Machine](http://wiki.unity3d.com/index.php?title=Finite_State_Machine) by Unity Wiki does provide overridable functions to be executed when entering and exiting states. However, we also need to perform actions in `Update`, `FixedUpdate` and similar functions for entities that have time-based changes such as a player, enemies, NPC and so on. So this implementation is not sufficient.

[Unity3D Finite State Machine](https://github.com/thefuntastic/Unity3d-Finite-State-Machine) satisfies functionality requirements. It provides on enter/exit functions as well as `Update`, `FixedUpdate`, `LateUpdate`. It does not use separate `State` class, instead, it uses reflection to call the correct function in the main Component for each state. Therefore, all functions of all states must be defined in the main Component, for instance, `Play_Enter`, `Play_Exit`, `Init_Enter`, `Init_Exit`, `Move_Enter`, `Move_Exit`.

My own implementation of [Finite State Machine](https://github.com/minhhh/unity-fsm) is similar to the above method, except that I don't want to use generics, since it will make it harder to refer to the `FSM` using code.

Another way to implement FSM is to make each state a separate MonoBehaviour. In this way, you can separate the functions for each state in its own file. In addition, you can examine the states in the Editor easily, like other MonoBehaviour. One issue which needs to be solved is how to access the members of the main Component. So you have to pass in the main Component to the state via constructor and make the members public. An alternative way is to write generic singletons which can be accessed from anywhere.


## References
* [Unity3D Finite State Machine](https://github.com/thefuntastic/Unity3d-Finite-State-Machine)
* [Finite State Machine](http://wiki.unity3d.com/index.php?title=Finite_State_Machine)
* [A simple finite state machine with C# delegates in Unity](http://www.voidinspace.com/2013/05/a-simple-finite-state-machine-with-c-delegates-in-unity/)
* [Using Interfaces to Make a State Machine for AI](https://unity3d.com/learn/tutorials/topics/scripting/using-interfaces-make-state-machine-ai)
