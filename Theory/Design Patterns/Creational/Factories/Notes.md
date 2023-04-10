# Notes: Factory Patterns
---

> A Factory is a component responsible solely for the wholesale (not piecewise) creation of objects.

- Factories are used as means to provide interfaces for creating objects.

- A factory will receive some information about a required object, instantiate it and return it.

Depending on the nature of the outsource one can define three types of factory patterns.
1. Outsource to a separate method (**Factory Method**)
2. Outsource to a separate class (**Factory**)


## Problem

As a code base grows it may find that some classes are coupled to the functionality and therefore a new implementation means conditional statements that define the object needed based on some previous conditions.
This along with some initializers that require a high amount of flags or conditions to instantiate an object make the code base tangled and not easily scalable.

- Creation logic becomes too convoluted.
- Complexity grows as tighly coupled classes make new features impossible.
- Code filled with conditionals deciding which class to use for every case.
- Many classes exist that have simmilar functionality.

## Solution

The solution in this case is to outsource the creation of a product to a creator (factory) which is responsible for receiving some info on the object and returning the required one.

![Solution](https://refactoring.guru/images/patterns/diagrams/factory-method/structure-indexed.png)

1. The product declares an interface that is common for all concrete.

2. All concrete products then are created based on that interface.

3. The creator declares the factory method.
    - it instantiates the object and returns it (the concrete product)
    - it can have abstract methods for concrete creators based on some extra logic needed for the creation of a concrete product.

4. If needed concrete creators are created to return the specific product with the logic of the initialization defined here.

## Uses

- As it separates object creation with the actual usage of the objects it is easier to extend and add concrete classes of creators/products as needed.

- This means that we do not need to know beforehand the exact types or dependecies of the objects.

## Pros and Cons

Pros:
- Avoids tight coupling in the code base.
- Single Responsibility Principle, the creation is assigned to a constructor while the usage is delegated to the code.
- Open/Closed principle, new types of products are introduced by inheritance

Cons:
- the code may become more complex by including classes and hierarchies.