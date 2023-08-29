class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next: Node | None = None

    def __repr__(self) -> str:
        return f"Node with value: {self.value} points to {self.next}"


class LinkedListStack:
    def __init__(self) -> None:
        self.head = None
        self.tail: Node | None = None
        self.length = 0

    def peek(self):
        return self.tail

    def push(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length += 1

        else:
            current_node = self.head
            self.head = new_node
            self.head.next = current_node
            self.length += 1

        return self

    def pop(self):
        if self.length <= 1:
            return None

        self.head = self.head.next
        self.length -= 1
        return self

    def print_values(self):
        current_node = self.head
        res = []
        while current_node:
            res.append(current_node.value)
            current_node = current_node.next
        return res

class ArrayStack:

    def __init__(self) -> None:
        self.data = []

    def push(self, value):

        self.data.append(value)
        return self

    def pop(self):

        self.data.pop()
        return self

    def peek(self):

        return self.data[-1]

    def print_values(self):
        return self.data

class QueueByStack:

    def __init__(self):
        self.data = ArrayStack()

    def push(self, value):
        self.data.push(value)


    def pop(self):
        self.data.data.pop(0)

    def peek(self):
        return self.data.data[0]


    def print_values(self):
        return self.data.print_values()

if __name__ == "__main__":
    # stack = LinkedListStack()
    stack = ArrayStack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.peek())
    print(stack.print_values())
    stack.pop()
    print(stack.peek())
    print(stack.print_values())

    print("-------------")
    queue = QueueByStack()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.pop()
    print(queue.peek())
    print(queue.print_values())

