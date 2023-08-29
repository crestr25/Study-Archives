from typing import Optional


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.previous = None

    # def __repr__(self):
    #     return f"Node with value {self.value} points to {self.next}, and back {self.previous}"


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self) -> str:
        return f"doubly linked list with head: {self.head}"

    def append(self, value):
        node = Node(value)

        if not self.head:
            self.head = node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = node
            node.previous = current_node

        self.length += 1

    def prepend(self, value):
        node = Node(value)

        if not self.head:
            self.head = node
        else:
            self.head.previous = node
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
            node.previous = current_node
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

if __name__ == "__main__":

    # Test Doubly Linked List
    ll = DoublyLinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(6)
    ll.append(7)
    ll.append(9)
    ll.prepend(0)
    print(ll)
    ll.insert(5, 666)
    print(ll.print_list())
    # ll.delete(6)
    # print(ll.print_list())
