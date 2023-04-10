class SingletonMeta(type):
    """
    The singleton class.

    Note that there are multiple approaches to creating a singleton:
        - Base class
        - Decorator
        - Meta Class
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Changes to the value of the __init__ argument do not affect the returned instance
        since the class attr is used
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    

class SingletonA(metaclass=SingletonMeta):
    def business_logic(self):
        """
        Any Singleton should define some bussiness logic, which can be executed on its instance.
        """
        ...

    def __str__(self):
        return "Singleton A"


class SingletonB(metaclass=SingletonMeta):
    def business_logic(self):
        """
        Any Singleton should define some bussiness logic, which can be executed on its instance.
        """
        ...
    def __str__(self):
        return "Singleton B"

if __name__ == "__main__":
    # The client code.

    sa1 = SingletonA()
    sa2 = SingletonA()
    
    sb1 = SingletonB()
    sb2 = SingletonB()


    if id(sa1) == id(sa2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")

    if id(sb1) == id(sb2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")

    if id(sa1) == id(sb2):
        print("Singleton failed, variables that inherit point to the same")
    else:
        print("Singleton works, both variables contain a different singleton.")
