from typing import Optional


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node with value {self.value} points to {self.next}"


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.length = 0

    def __repr__(self) -> str:
        return f"linked list with head: {self.head}"

    def append(self, value):
        node = Node(value)

        if not self.head:
            self.head = node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = node

        self.length += 1

    def prepend(self, value):
        node = Node(value)

        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def print_list(self):
        val_array = []
        current_node = self.head
        while current_node:
            val_array.append(current_node.value)
            current_node = current_node.next
        return val_array

    def insert(self, index, value):
        if index > self.length:
            raise IndexError

        node = Node(value)

        if index == 0:
            node.next = self.head
            self.head = node
        else:
            c = 1
            current_node = self.head
            while c < index:
                current_node = current_node.next
                c += 1
            node.next = current_node.next
            current_node.next = node 

    def delete(self, index):
        c = 0
        current_node = self.head
        while c < index - 1:
            current_node = current_node.next
            next_node = current_node.next
            c += 1
        current_node.next = next_node.next 
        self.length-=1

    def reverse(self):
        current_node = self.head
        prev_ref = None
        new_ref = None
        while current_node:
            prev_ref = current_node.next
            current_node.next = new_ref

            new_ref = current_node
            current_node = prev_ref

        self.head = new_ref

if __name__ == "__main__":
    # Test nodes
    # print(Node(4))

    # Test Linked List
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(6)
    ll.append(7)
    ll.append(9)
    ll.prepend(0)
    ll.insert(5, 666)
    print(ll.print_list())
    ll.delete(6)
    print(ll.print_list())
    ll.reverse()
    print(ll.print_list())
