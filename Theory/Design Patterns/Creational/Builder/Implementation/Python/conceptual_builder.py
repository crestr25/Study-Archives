from abc import ABC, abstractmethod


#######################
## BUILDER INTERFACE ##
#######################

class Builder(ABC):
    """
    Here we specify the different 
    methods to create the product
    """

    @property
    @abstractmethod
    def product(self): pass

    @abstractmethod
    def process_a(self): pass

    @abstractmethod
    def process_b(self): pass

    @abstractmethod
    def process_c(self): pass

    @abstractmethod
    def reset(self): pass

######################
## CONCRETE BUILDER ##
######################

class ConcreteBuilderA(Builder):
    """
    The Concrete Builder

    Follows the Builder interface and defines the specific
    implementations of the buildings steps defined.
    """

    def __init__(self):
        """
        A fresh instance of a builder should contain a blank
        product to construct.
        """
        self.reset()

    def reset(self):
        self._product = Product1()

    @property
    def product(self):
        """
        Get the Product

        This method should be implemented in the concrete builders as it is 
        specified in the Notes.md, however, python being dinamically typed allows to
        specify this as a property.

        In this method (also getResult/getProduct) we reset the current product to
        leave the constructor ready for a new assembly and we return
        the created object.
        """
        product = self._product
        self.reset()
        return product
    

    def process_a(self):
        self._product.add("PartA1")


    def process_b(self):
        self._product.add("PartB1")


    def process_c(self):
        self._product.add("PartC1")

##############
## PRODUCTS ##
##############

class Product1():
    """
    Product

    When the configuration of a product is complex and requires extensive
    a bunch of parameters and flags to set.

    Does not require to inherit from a common interface since builders
    can produce unrelated products.
    """

    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        print(f"Product parts: {', '.join(self.parts)}")

##############
## DIRECTOR ##
##############

class Director:
    """
    Director
    
    The director is in charge of executing the steps in order for the builder to
    produce the object.

    It is optional since one could always just run the steps in the builder
    to get the product.

    It is used to abstract the logic of the creation and make the client
    work directly with the client.
    """
    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder
    
    @builder.setter
    def builder(self, builder):
        """
        The director can work with any builder instance passed
        by the client
        """
        self._builder = builder


    """
    We can have different product variations with the same building
    steps.
    """
    def build_small_product(self):
        self.builder.process_a()

    def build_medium_product(self):
        self.builder.process_a()
        self.builder.process_b()

    def build_large_product(self):
        self.builder.process_a()
        self.builder.process_b()
        self.builder.process_c()

if __name__ == "__main__":
    """
    Here the client code:
        - Creates the Builder object
        - Passes it to the director / Calls the methods in order
        - The end result is retrieved from the builder object.
    """
    director = Director()
    builder_a = ConcreteBuilderA()
    director.builder = builder_a

    print("Small Product")
    director.build_small_product()
    builder_a.product.list_parts()

    print("Medium Product")
    director.build_medium_product()
    builder_a.product.list_parts()

    print("Large Product")
    director.build_large_product()
    builder_a.product.list_parts()

