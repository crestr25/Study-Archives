# Notes: Builder Pattern
---
> Allows construction of complex objects step by step.

The Builder is one of the **Creational** design pattern that focuses on:
- The construction of complex objects step by step.
- Allow the production of different types and representations of an object using the same construction code.<br>

## Problem

when building complex classes one downside is initializing the contructor to instantiate the object<br>
As the codebase gets bigger and more complex the implementation to initialize an object can be separated in two ways.
- A god constructor, which is a parameter hell to create from every combination available of an object.
- Scattered code which either extends or modifies the original class.

## Solution

To create a solution to this problem the builder design patter extracts the object construction into a set of **steps** that are defined in a new constructor object.

To create an object one just executes this steps on a builder object or create a Director which completely hides the construction details from the client. (The important note here is that the call should be only for the steps that are necessary for that object).

![Solution](https://refactoring.guru/images/patterns/diagrams/builder/structure-indexed.png?id=44b3d763ce91dbada5d8394ef777437f)

1. The builder interface declares the methods to construct a new product. (this is the base which contains all steps required to build an abstract object).

2. A concrete builder is created which now provides the implementation to the methods required. It returns the product with all the steps required for it's construction.

3. The products are the results of the concrete builders. (These products do not have to follow a common interface or hierarchy)

4. The Director defines the order in which to call the construction steps, it can also be used to reuse specific configurations (Note that by not having the director one would have to call the steps manually, this director object hides that implementation to the client).

5. The client can:
    - call the director associating it with a builder object and use it exclusively.
    - Call the desired builder on the production method which would allow to use multiple builders.
    - Call the steps on the builder directly.

## Uses

- To get rid of a Constructor with many parameters/flags, The builder pattern will make use of the step by step process to instantiate objects depending on the required setup of methods.

- When the code base requires different representations of a product, this means that the steps to create it are very similar but the difference is in the details.

- Can be used to build Composite objects (Structural Design Patter), since the builder does not expose the product until it is done.

## Pros and Cons

Pros:
- objects are constructed step by step. (can be run recursively/Composite objects.)

- A constructor can now be reused.

- Single Responsibility Principle as one can extract product creation code into one place.

Cons:

- The pattern requires multiple classes which makes the complexity of the code grow.