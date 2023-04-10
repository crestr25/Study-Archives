# Notes: Adapter
---

> Allow objects with incompatible interfaces to collaborate

- Basically a construct which adapts an existing interface X to conform to the required interface Y.

- It means, An adapter allows two incompatible interfaces to work together without modifying the internals of each component.

- Similar to a power adapter that turns a (US socket to a EU socket). Instead of just modifying the plugs of all of our machines

## Problem

Trying to adapt a new class to an existing code may provide a problem in which the two interfaces don't match, meaning that they require different inputs to work. In other words

1. The classes are not compatible and to adapt one some changes would be required that could break some other part of the code.
2. One could be working with a 3rd party class which does not provide the source code, making the process harder to be implemented.

## Solution

The solution to the problem is to.

1. Generate a special object `Adapter` which converts the interface of the desired objects to work.
2. It wraps the object and hides the complexity of the conversion so the classes just call the adapter and receive the expected outcome.

![Solution](https://refactoring.guru/images/patterns/diagrams/adapter/structure-object-adapter-indexed.png)

## Uses

- When using a class with an incompatible interface.
- One could also use it to reuse several existing subclasses that lack some common functionality by wrapping them and giving the desired functionality (similar to the decorator patter)

## Pros and Cons

Pros:
- Uses the single responsibility principle by separating the interface or data conversion code from the bussiness logic part of the program.
- Open/closed principle, as one can introduce functionality to an existing class without modifying it.

Cons:
- Added complexity, as new interfaces and classes are added. Keep in mind that changind the service class its sometimes easier and less time consuming.
