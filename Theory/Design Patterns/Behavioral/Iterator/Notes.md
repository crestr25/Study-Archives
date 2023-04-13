# Notes: Iterator
---

> A class that facilitates the traversal of data structures.

- It keeps a reference to the current element.
- It knows how to move to a different element.

## Problem

- There are many types of collections in which to store elements. (lists, stacks, trees, graphs, etc).

- These collection no matter the implementation must provide a way of accessing each element for use.

- The primary responsibility of a collection is to provide an efficient way to store elements, however, one may want to traverse these collections.
    - One would want to have a way of knowing the current element, meaning that a new iteration is not required every time the next element is needed.
    - One would want to abstract the algorithm used for the traverse and implement various depending on the context.

- Implementing these functionality in a collection the single responsibility principle is broken and our code ends up coupled to specific classes for each traverse algorithm.

## Solution

- The main idea is to separate the traverse behavior into a separate object which will be the **ITERATOR**.

- The **ITERATOR** will have the responsibility of:
    - Implementing the algorithm.
    - Keep track of the current position.
    - Keep track of the elements left.

- When a new algorithm is used to traverse a collection a new **ITERATOR** is created and the client code can use it without any extra implementation, the elements will just be yielded in the new implemented order.

- All **ITERATOR** must implement the same interface.

![Solution](https://refactoring.guru/images/patterns/diagrams/iterator/structure-indexed.png)

1. The iterator interface declares all operations required to traverse the element.
    - get next element.
    - get current position.
    - restart an iteration.
    - ...

2. A concrete iterator implements the specific traversal algorithm used to traverse the collection.
    - The concrete iterator should hold the state of the iteration so other iterators can work on the collection.

3. The collection interface declares the methods to get an iterator that is compatible with said collection.
    - The return type of the method to get an iterator points to the interface of an iterator so that concrete collections can implement different kinds of iterators.

4. The concrete collection return a new instance of a concrete iterator every time the client requests one.

5. The client works with the iterator and collection via their interfaces preventing the client from coupling to a concrete class.
    - Usually the client gets an iterator from the collection and not directly.

## Uses

- 

## Pros and Cons

Pros:
- 

Cons:
- 
