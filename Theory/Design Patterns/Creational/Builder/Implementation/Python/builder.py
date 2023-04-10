from abc import ABC, abstractmethod

# Product

class Guitar:

    def __init__(self):
        self.__body = None
        self.__neck = None
        self.__bridge = None
        self.__strings = None

    def set_body(self, body):
        self.__body = body

    def set_neck(self, neck):
        self.__neck = neck

    def set_bridge(self, bridge):
        self.__bridge = bridge

    def set_strings(self, strings):
        self.__strings = strings

    def __str__(self):
        return f"""Awesome guitar with 
        body: {self.__body},
        neck: {self.__neck},
        bridge: {self.__bridge},
        strings: {self.__strings}
        """


# Builder Interface
class GuitarBuilder(ABC):

    @abstractmethod
    def get_body(self):
        pass

    @abstractmethod
    def get_neck(self):
        pass

    @abstractmethod
    def get_bridge(self):
        pass

    @abstractmethod
    def get_strings(self):
        pass


# Concrete Builders
class ElectriGuitarBuilder(ABC):
    
    def get_body(self):
        return "Awesome black finished body"

    def get_neck(self):
        return "Beautiful classic Rosewood neck"

    def get_bridge(self):
        return "Floyd rose bridge that stays in tune"

    def get_strings(self):
        return "Perfect .10 gauge strings"
    
    def get_connections(self):
        return "all pickups"


# Concrete Builders
class AcousticGuitarBuilder(ABC):
    
    def get_body(self):
        return "Awesome black finished body"

    def get_neck(self):
        return "Beautiful classic Rosewood neck"

    def get_bridge(self):
        return "Floyd rose bridge that stays in tune"

    def get_strings(self):
        return "Perfect .10 gauge strings"
    

# Director
class Director:

    __builder = None
    def set_builder(self, builder):
        self.__builder = builder

    def get_guitar(self):
        guitar = Guitar()

        guitar.set_body(self.__builder.get_body())
        guitar.set_bridge(self.__builder.get_bridge())
        guitar.set_neck(self.__builder.get_neck())
        guitar.set_strings(self.__builder.get_strings())

        return guitar
    

if __name__ == "__main__":
    director = Director()
    director.set_builder(ElectriGuitarBuilder())
    my_guitar = director.get_guitar()
    print(my_guitar)



