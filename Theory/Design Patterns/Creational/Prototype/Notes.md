# Notes: Prototype
---

> Lets one copy existing objects without making the code dependent on their classes.

Make copies of an existing object by delegating the process to that object.

## Problem

To make a copy of an existing object one would have to have access to the object's internal attributes and copy them exactly. This is not optimal since.

1. The object may have some private fields that are not visible unless one has access to the object class.
2. That would make the object dependent on that class. And that class may not be available, just its interface.

## Solution

The solution to the problem is to.

1. Delegate the cloning process to the actual objects that are being cloned.

This means creating a `clone` method that takes care of the logic of the cloning and decoupling it from the logic of another object.

- Objects of the same class can access its hidden attributes.
- The process would be straightforward.

An object that supports cloning is therefore called `Prototype`

![Solution](https://refactoring.guru/images/patterns/diagrams/prototype/structure-indexed.png)

1. The prototype interface defines the the clone method (or methods) to be used to duplicate the object.

2. The concrete prototypes that implement those clone methods are created.
    - Here one can handle the edge cases of a cloning process, such as cloning all linked objects and recursive dependencies.

3. The client can produce a copy of any object 

## Uses

- The principal use is when the code does not need to depend on the concrete classes of the objects that are being copied, therefore no tight coupling is generated.
- A prototype is then created for a third party object to be copied and used without needing the hidden details of its implementation.
- Create a registry of objects that require some different configurations to be instantiated, this way the logic stays in one place, and to use one just clone from that prototype.

## Pros and Cons

Pros:
- Clone objects without coupling to the concrete class.
- Replace repeated initialization with built-in prototypes.
- Complex objects can be easily reproduced.
- Alternative to inheritance when dealing with configuration presets from complex objects. (no need to couple with hierarchy)

Cons:
- Cloning objects with circular references.
