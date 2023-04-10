# Notes: Abstract Factory Patterns
---

> An Abstract factory defines interfaces to create families of related object without specifying their concrete classes.

- An abstract factory lets one produce an interface to generate classes of the same related family.

- It is used for effectively work with closely related families of different products that have variants associated with them.
    - Factories usually just work with a single type of product.

- The client is not interested in the concrete class of the factory it works with.


## Problem

When a codebase consist of different family of related classes which in turn have several variants of each class. One ends up with a requirement on how to add aditional classes that correctly match the family and variant.

- 

## Solution

Given that the code is split up in:
    - Product family
    - Variants

The abstract factory tries to generalize the object creation by setting an interface for initializing them (an abstract factory), each variant is then concretely instantiated by the concrete factories that are created.

![Solution](https://refactoring.guru/images/patterns/diagrams/abstract-factory/structure-indexed.png)

1. The abstract products declare an interface that defines related products that make a family.

2. Concrete products are the implementations of those abstract products (Must create one for all variants).

3. The abstract factory interface declares the methods needed to create those abstract products.

4. Now the concrete factories implement the actual creation methods for each of the variants of a family of concrete products.

Note: The concrete factories must have signatures for the abstract product, this way no actual coupling of a concrete class and a client is created.

## Uses

- When a codebase is made of various families of related products, this allows for extensibility as not all families are required beforehand.

- When a set of factory methods implement logic that instantiates multiple product types.

## Pros and Cons

Pros:
- All products that are returned by a factory are compatible.

- Avoid tight coupling between concrete products and client code.

- Single Responsibility Principle as one can extract product creation code into one place.

- Open/Closed Principle as new variants of a product can be created without breaking existing code

Cons:

- Many new classes may complicate the codebase and make it less readable