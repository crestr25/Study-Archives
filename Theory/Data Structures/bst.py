"""BINARY SEARCH TREE"""
COUNT = [10]


def print2DUtil(root, space):
    # Base case
    if root == None:
        return

    # Increase distance between levels
    space += COUNT[0]

    # Process right child first
    print2DUtil(root.right, space)

    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.value)

    # Process left child
    print2DUtil(root.left, space)


# Wrapper over print2DUtil()


def print2D(root):
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)


class Node:
    def __init__(self, value) -> None:
        self.left: Node | None = None
        self.right: Node | None = None
        self.value = value

    # def __repr__(self) -> str:
    #     return f"{self.value}, {self.right}, {self.left}"


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if not self.root:
            self.root = new_node
            return self

        current_node = self.root

        while True:
            if new_node.value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break
        return self

    def lookup(self, value):
        if not self.root:
            return None

        current_node = self.root

        while current_node:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                return current_node

    def remove(self, value):
        if not self.root:
            return None

        parent = None
        child = self.root

        while child:
            if value < child.value:
                parent = child
                child = child.left
            elif value > child.value:
                parent = child
                child = child.right
            else:
                break

        new_parent = child
        new_child = new_parent.right if value > new_parent.value else new_parent.left

        while new_child:
            if new_child.left:
                new_parent = new_child
                new_child = new_child.left
            else:
                break

        new_parent.left = None

        if parent.right.value == child.value:
            new_child.right = child.right
            new_child.left = child.left
            parent.right = new_child
            return self
        if parent.left.value == child.value:
            new_child.right = child.right
            new_child.left = child.left
            parent.left = new_child
            return self

    def breadthFirstSearch(self):
        current_node = self.root
        result = []
        queue = []

        queue.append(current_node)

        while queue:
            current_node = queue.pop(0)
            result.append(current_node.value)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return result

    def depthFirstSearch_inorder(self):
        return traverse_inorder(self.root, [])

    def depthFirstSearch_preorder(self):
        return traverse_preorder(self.root, [])

    def depthFirstSearch_postorder(self):
        return traverse_postorder(self.root, [])
    

def traverse_inorder(node, result):
    if node.left:
        traverse_inorder(node.left, result)
    result.append(node.value)
    
    if node.right:
        traverse_inorder(node.right, result)
    return result

def traverse_preorder(node, result):
    result.append(node.value)

    if node.left:
        traverse_preorder(node.left, result)
    
    if node.right:
        traverse_preorder(node.right, result)
    return result

def traverse_postorder(node, result):
    if node.left:
        traverse_postorder(node.left, result)
    
    if node.right:
        traverse_postorder(node.right, result)
    result.append(node.value)
    return result

if __name__ == "__main__":
    bst = BinarySearchTree()

    bst.insert(9)
    bst.insert(4)
    bst.insert(20)
    bst.insert(1)
    bst.insert(6)
    bst.insert(15)
    bst.insert(170)
    print2D(bst.root)
    # bst.remve(4)
    # bst.remove(20)

    # print2D(bst.root)
    print(bst.breadthFirstSearch())
    print(bst.depthFirstSearch_inorder())
    print(bst.depthFirstSearch_preorder())
    print(bst.depthFirstSearch_postorder())
    # print(f"Node - {bst.lookup(15)}")
