# Notes: Bridge
---

> A mechanism that decouples an interface (hierarchy) from an implementation (hierarchy)

- Split a large class, or set of closely related classes into two separate hierarchies that are developed independent of each other.

- the two hierarchies are usually
    - Abstraction, which means the code that interacts with (high-level control layer) the client and delegates the work to the implementation.
    - Implementation, which is the part with the actual bussiness logic.

- It prevents a Cartessian product complexity explosion. 


## Problem

When creating classes that inherit from an existing codebase, or creating functionality that has a high number of dimensions (features) that must work together.

Usually it will end up looking like this, a cartessian product with highly coupled functionality between the features.

![Solution](https://refactoring.guru/images/patterns/diagrams/bridge/problem-en.png)

This implies that a better approach would be to instead separate the classes by features and link them together by a reference.

![Solution](https://refactoring.guru/images/patterns/diagrams/bridge/solution-en.png)

## Solution

The solution to the problem is to.

1. Split the classes in two hierarchies.
    - One with the logic that controls the base of a class
    - One with the actual implementation.
2. This way the classes will be independent of each other and will be linked through a reference between hierarchies, thus eliminating the underlying problem of a cartessian product of classes.

![Solution](https://refactoring.guru/images/patterns/diagrams/bridge/structure-en-indexed.png)

1. The abstraction provides the high-level control logic. it relies on the link to the implementation to actualy make the low-level work.

2. The implementation declares the interface for all concrete implementations to follow.

3. The concrete implementations contain the specific code.

4. This refined abstractions are optional and are meant to provie variants to the control logic. (they make use like the parents of the implementation interface)

5. The client works with the abstraction, However, it is also the client the one responsible for linking the abstraction object to one of the implementations.


## Uses

- The bridge pattern lets one split a monolithic class into several class hierarchies (not one), this approach lets one change the classes in each of the hierarchies independently of the classes in the others.

- When a class needs to be extended in several dimensions, this approach separates the hierarchies and connects them with a reference.

## Pros and Cons

Pros:
- Open/closed principle, new abstractions and implementations independent from each other

- Single responsibility principle, each hierarchy is responsible for one of the dimensions.

- The client code works with the (abstraction/interface) and not the (implementation/API)

Cons:
- Added complexity, as the code can be made more complicated on a highly cohesive class.
