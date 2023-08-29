class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next: None | Node = None

    def __repr__(self) -> str:
        return f"Node with value: {self.value} points to {self.next}"

class LinkedListQueue:

    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, value):
        new_node = Node(value)

        if not self.first:
            self.first = new_node
            self.last = new_node
            self.length += 1
            return self

        self.last.next = new_node
        self.last = new_node
        self.length += 1

        return self


    def dequeue(self):
        
        self.first = self.first.next
        self.length -= 1
        return self


    def peek(self):

        if self.length <= 1:
            return None

        return self.first

    def print_values(self):

        arr = []
        next_value = self.first

        while next_value:
            arr.append(next_value.value)
            next_value = next_value.next

        return arr


if __name__ == "__main__":

    queue = LinkedListQueue()
    queue.enqueue("Joy")
    queue.enqueue("Matt")
    queue.enqueue("Pavel")
    queue.enqueue("Samir")
    print(queue.peek())
    queue.dequeue()
    print(queue.print_values())


