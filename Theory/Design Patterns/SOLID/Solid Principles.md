# SOLID Principles

These are five software principles that serve as guidelines to follow when building software that is easier to scale and mantain.

---

## 1. Single Responsibility Principle (SRP)

### Definition

>A class should have one and only one reason to change, meaning that a class should have only one job.

This means that if a class has more than one responsibility, it becomes coupled. Meaning, a change to one of the responsibilities results to modification of the other responsibilities.

To implement this principle one should design classes in a manner that all related features are together, meaning that most of their properties and their attributes are used by their methods, so whenever a change is needed they change for the same reason.   

If there are different changes stated it probably means that an abstraction is missing.

The antipattern for this is commonly known as the GOD CLASS, which is a software component that knows too much (many attributes/properties) or does too much (many methods/functions)

### Examples

#### a. Python

```python
class Animal:
    def __init__(self, name: str):
            self.name = name
    
    def get_name(self):
        pass


class AnimalDB:
    def get_animal(self) -> Animal:
        pass

    def save(self, animal: Animal):
        pass
```

---

## 2. Open-Closed Principle (OCP)

>Software Entities (Classes, Modules, Functions) should be opened for extension and closed for modification.

The Principle aims at extension of behaviours without changing the existing behaviour of that class.

By changing the behaviour of an entity we will modify ALL systems using that entity, to avoid this the principle states that all modification should be made by extension. Meaning, add to the functions that already exist NOT change them.

### Examples

#### a. Python
```python
from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, name: str, salary: str):
        self.name = name
        self.salary = salary

    @abstractmethod
    def work(self):
        pass


class Tester(Employee):

    def __init__(self, name: str, salary: str):
        super().__init__(name, salary)

    def test(self):
        print("{} is testing".format(self.name))

    def work(self):
        self.test()

class Developer(Employee):

    def __init__(self, name: str, salary: str):
        super().__init__(name, salary)

    def develop(self):
        print("{} is developing".format(self.name))

    def work(self):
        self.develop()

class Company:

    def __init__(self, name: str):
        self.name = name

    def work(self, employee: Employee):
        employee.work()



carbon = Company("Carbon")
developer = Developer("Nusret", "1000000")
tester = Tester("Someone", "1000000")
carbon.work(developer) # Will print Nusret is developing
carbon.work(tester) # Will print Someone is testing
```
---

## 3. Liskov Substitution Principle (LSP)

### Definition

>If S is a subtype of T, then objects of type T may be replaced by objects of type S, without breaking the program.

The aim of this principle is to make sure a sub-class can assume the place of its super-class without any errors.

If in a subclass, you redefine a function that is also present in the base class, the two functions should have the same behaviour. Not meaning that they should be equal but the same type of result should be given when the same input is received.

This Principle aims at code that is consistent and the end-user will need to learn how the code works only once

### Examples

#### a. Python
```python
from abc import ABC, abstractmethod
from typing import List

class Member(ABC):
    # Students, Teachers and managers are all members of school
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # They all have a method to store to the db
    @abstractmethod
    def save_database(self):
        pass

class Payer(ABC):
    # Students do not pay, but it makes sense that they are
    # members so we need a payer class for the members that pay
    @abstractmethod
    def pay(self):
        pass

# Teacher inherits from member and payer
class Teacher(Member, Payer):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id

    def save_database(self):
        print("Saving teacher data to database")

    def pay(self):
        print("Paying")

# Manager inherits from member and payer
class Manager(Member, Payer):
    def __init__(self, name, age, manager_id):
        super().__init__(name, age)
        self.manager_id = manager_id

    def save_database(self):
        print("Saving manager data to database")

    def pay(self):
        print("Paying")

# Student only inherits from member
class Student(Member):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def save_database(self):
        print("Saving student data to database")

members: List[Member] = []
members.apped(Student('nusret',23,"12345"))
members.apped(Teacher('Teacher_nusret',23,"12345"))
for member in members:
	member.save_database()

payers: List[Payer] = [Teacher("John", 30, "123"), Manager("Mary", 25, "456")]
for payer in payers:
    payer.pay()
```
---

## 4. Interface Segregation Principle (ISP)

### Definition

>Many client-specific interfaces are better than one general-purpose interface.

>>Note: An interface is considered, all the methods and properties "exposed", thus, everything that a user can interact with that belongs to that class.

This means, Clients should not be forced to depend on methods that they do not use. 

Instead of designing one big interface, one should create interfaces as small as possible each one serving a specific sub-module.

This principle deals with the disadvantages of implementing big interfaces.

### Examples

#### a. Python
```python
from abc import ABC, abstractmethod

class Walker(ABC):
  @abstractmethod
  def walk() -> bool:
    return print("Can Walk") 

class Swimmer(ABC):
  @abstractmethod
  def swim() -> bool:
    return print("Can Swim") 

class Human(Walker, Swimmer):
  def walk():
    return print("Humans can walk") 
  def swim():
    return print("Humans can swim") 

class Whale(Swimmer):
  def swim():
    return print("Whales can swim") 

if __name__ == "__main__":
  Human.walk()
  Human.swim()

  Whale.swim()
  Whale.walk()

# Humans can walk
# Humans can swim
# Whales can swim
```

---

## 5. Dependency Inversion Principle (DIP)

### Definition

> Abstractions should not depend on details. Details should depend on abstraction. High-level modules should not depend on low-level modules. Both should depend on abstractions.

This means that abstractions(e.g interfaces) should not be dependent on low-level methods but both of them should depend on a third middle interface.

The principle states that a class should not be fused with the tool it uses to execute an action. Rather, it should be fused to the interface that will allow the tool to connect to the class.

This principle aims at reducing the dependency of a high-level class on the low-level class by introducing an interface.



### Examples

#### a. Python
```python

from abc import ABC, abstractmethod


class EventSender(ABC):
    @abstractmethod
    def send(self, event):
        pass


class Syslog(EventSender):

    def write(self, msg):
        with open('path', 'a') as f:
            f.write(msg)

    def send(self, event):
        self.write(event)


class EventStreamer:
    def __init__(self, sender: EventSender):
        self.event_stream = sender

    def send_event(self, event):
        self.event_stream.send(event)
```