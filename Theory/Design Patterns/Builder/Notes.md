# Notes: Builder Pattern
---
The Builder is one of the **Creational** design pattern that focuses on:
- The construction of complex objects step by step.
- Allow the production of different types and representations of an object using the same construction code.<br>

## Problem

when building complex objects one tends to create a constructor with many parameters and flags to instantiate it.<br>
Though there are many ways to mitigate this the result is usually a large number of subclasses to cover all combinations of parameters and adding more as more products are designed. Or worse leaving the constructor as a large unused lot of flags and parameters.

## Solution

To create a solution to this problem the builder design patter organizes the object construction into a set of **steps**, and to create an object one just executes this steps on a builder object. (The important note here is that the call should be only for the steps that are necessary for that object).

![Solution](https://refactoring.guru/images/patterns/diagrams/builder/structure.png)

## Uses

- To get rid of a Constructor with many parameters/flags, The builder pattern will make use of the step by step process to instantiate objects depending on the required setup of methods.

- 