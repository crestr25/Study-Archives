from abc import ABC, abstractmethod

class Abstraction(ABC):
    """
    The abstraction interface

    Defines the control part of the two hierarchies.

    Mantains a reference to an object of the implementation hierarchy and
    delegates all real work to this object.
    """
    def __init__(self, implementation):
        self.implementation = implementation

    def operation(self):
        return f"""calling operation: \n
        actual work from the implementation {self.implementation.operation_implementation()}"""


class RefinedAbstraction(Abstraction):
    """
    The Abstraction can be refined without changing the implementation class
    """
    def operation(self):
        return f"""calling Refined operation: \n
        actual work from the implementation {self.implementation.operation_implementation()}"""

class Implementation(ABC):
    """
    The implementation interface

    Defines the primitive operations to call from the high-level operations from
    the abstraction class
    """
    @abstractmethod
    def operation_implementation(self):
        pass

class ConcreteImplementationA(Implementation):
    """
    Each concrete implementation corresponds to a specific solution to an implementation

    - specific Platform
    - specific Tool
    """

    def operation_implementation(self):
        return "Hello From the A Side"

class ConcreteImplementationB(Implementation):
    """
    Each concrete implementation corresponds to a specific solution to an implementation

    - specific Platform
    - specific Tool
    """

    def operation_implementation(self):
        return "Hello From the B Side"
    

def client_code(abstraction):
    """
    The client code

    Calls the abstraction class alone, meaning that it can now support any
    abstraction-implementation combination
    """
    print(abstraction.operation())

if __name__ == "__main__":
    """
    The client code is also responsible for linking all the

        Abstraction - Implementation 

    """
    implementation_a = ConcreteImplementationA()
    implementation_b = ConcreteImplementationB()
    abstraction_A = RefinedAbstraction(implementation_a)
    abstraction_B = RefinedAbstraction(implementation_b)

    client_code(abstraction_A)
    client_code(abstraction_B)