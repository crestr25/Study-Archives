# Notes: Factory Patterns
---

> A Factory is a component responsible solely for the wholesale (not piecewise) creation of objects.

- unlike the builder which requires piecewise creation, the factory tries to create the object completely by outsourcing the creation.

Depending on the nature of the outsource one can define three types of factory patterns.
1. Outsource to a separate method (**Factory Method**)
2. Outsource to a separate class (**Factory**)
3. Can create a hierarchy of factories (**Abstract Factory**).

## Problem

- creation logic becomes too convoluted.
- Initializer is not descriptive
    - Name is always `__init__`
    - Cannot be overloaded with same sets of arguments with different names.
    - Can turn into optional parameter hell (just like Builders).



## Solution


- Factory Methods.
    - We outsource the creation of the object to a method in order to provide an Api to the user.

    - This API helps provide a better naming to the initializer, arguments and solution that the class provides.

    - We eliminate the god init that verifies how to initialize based on conditions.

    - We "overload" the initializer.

- Factory
    - One problem that arises with Factory methods is that one could easily create many of them making the class clustered with initializers, by appliying the SRP and Separation of Concerns one can move those methods to a separate class.

    - 

- Abstract Factory
    - When the problem has a hierarchy of types, one can construct a corresponding hierarchy of factories.

    - The design would implement an abstract factory as a base class of other factories.

![Solution]()

## Uses

- 