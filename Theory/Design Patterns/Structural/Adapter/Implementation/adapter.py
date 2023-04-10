class Target:
    """
    We live in Colombia so the electronic's socket are two palets and ground
    """
    def connect(self):
        return "60hz: Connected"

class Adaptee:
    def eu_connect(self):
        return "50hz: Connected"

class Adapter:
    def __init__(self, machine):
        self._machine = machine

    def connect(self):
        self._machine.eu_connect()
        return "60hz: Connected"

def client_code(machine):
    """
    Client code that uses the connect interface
    """
    print(machine.connect())

if __name__ == "__main__":
    print("first target works with our client who wants to connect")
    target = Target()
    client_code(target)

    print("now we can also connect one adaptee with our adapter")
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    client_code(adapter)
    