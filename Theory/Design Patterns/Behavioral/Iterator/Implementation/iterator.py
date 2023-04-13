class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.right = right
        self.left = left
        self.value = value

        self.parent = None

        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

class InOrderIterator:
    def __init__(self, root):
        self.root = self.current = root
        self.yielded_start = False
        while self.current.left:
            self.current = self.current.left

if __name__ == "__main__":
    #    1
    #   / \
    #  2   3

    root = Node(1, Node(2), Node(3))
    print(root)
