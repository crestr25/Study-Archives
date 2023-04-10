from abc import ABCMeta, abstractmethod

# Product
class Console(metaclass=ABCMeta):
    """
    Here console would be our abstract product
    """
    @abstractmethod
    def play_game(self):
        pass

    @abstractmethod
    def update(self):
        pass

class Xbox(Console):
    def play_game(self):
        return "Man Halo is awesome"
    
    def update(self):
        return "Updating to latest xbox firmware"
    
class PS5(Console):
    def play_game(self):
        return "Man GOW Ragnarok rules"
    
    def update(self):
        return "Updating to latest ps5 firmware"
    
# Creator
class Creator(metaclass=ABCMeta):
    """
    Here console would be our abstract product
    """
    @abstractmethod
    def create_console(self):
        pass
        
class XboxCreator(Creator):
    def create_console(self):
        return Xbox()
    
class PS5Creator(Creator):
    def create_console(self):
        return PS5()

def console(prefered_console):
    if prefered_console == "xbox":
        return XboxCreator().create_console()
    elif prefered_console == "ps5":
        return PS5Creator().create_console()
    else:
        return f"{prefered_console} Not in stock"

if __name__ == "__main__":

    console1 = console("xbox")
    console2 = console("ps5")
    console3 = console("switch")

    print(console1.update(), console1.play_game())
    print(console2.update(), console2.play_game())
    print(console3)