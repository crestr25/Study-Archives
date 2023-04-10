# Notes: Singleton
---

> A component which is instantiated only once.

Singleton is a creational design pattern that lets the user instantiate the class only once, while providing a global access point to it.

For some componentes it makes sense to have a single instantiated object, instead of initializing a new one every time it is needed.

## Problem

1. One may have a resource that makes sense to instantiate one time like a db, or a file access.</br>
2. One may want to have a resource which can be accessed from any point in the program. </br>

## Solution

The solution to the problem is to.

1. Make the default constructor private (remember a constructor must always return a NEW object), this way one can hide the constructor and prevent other objects from using it directly.
2. Create a method that acts as a constructor.
    - This method calls the undelying constructor of the base class and saves the return object in a static field.
    - All calls to this method return that cached object.

![Solution](https://refactoring.guru/images/patterns/diagrams/singleton/structure-en-indexed.png)

1. The Singleton class declares the method to get the instance.
    - Note this method searches if the instance attribute is set and returns it or creates it, thus always having just one instance.

    - The constructor is hidden since it should always return a new object.

> Note: the Singleton pattern disables all other means of creating objects of a class except for the special cration method.

## Uses

- Mostly used to instantiate and access resources shared across the software like a db instance or a conection.
- When control is needed on global settings since the object can only be instantiated once.

## Pros and Cons

Pros:
- A class will have only one instance.
- Global access point to that instance.
- Only initialized when first requested.

Cons:
- Violates the single responsibility principle, it solves two problems.
- Can mask a bad design.
- Difficult to test, if the language uses inheritance for mocks.
- Requires special treatment with multithreading.