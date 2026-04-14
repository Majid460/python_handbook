# Binary Search Tree
"""
A Binary Search Tree is a binary tree with an extra rule:

Each node has at most 2 children (like a binary tree).

For every node:

All values in the left subtree are smaller than the node.

All values in the right subtree are greater than the node.

BST / Trees:
Ordered, range queries, successor/predecessor, dynamic sorted data.

O(log n) insert/delete/search (balanced tree).

Can be unbalanced → height O(n)
BST can become unbalanced, leading to O(n) search in worst case.
"""
from src.datastructures.linear_data_structure.lists.basic_info_list import count


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insertion in tree using loop
    def insert(self, data):
        new_node = Node(data)

        # Check if no root exist
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if new_node.data < current.data:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right

    # Insertion in tree using recursion
    def insertion_using_recursion(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insertion_using_recursion(root.left, data)
        elif data > root.data:
            root.right = self.insertion_using_recursion(root.right, data)
        return root

    def inorder(self, node: Node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    # Searching in Binary Search Tree
    def search(self, val: int) -> bool:
        current = self.root
        while current is not None:
            if val == current.data:
                return True
            elif val < current.data:
                current = current.left
            elif val > current.data:
                current = current.right
        return False

    # Find the minimum node
    def find_min_node(self) -> int:
        if not self.root:
            return -1
        current = self.root
        mini = self.root.data
        while current is not None:
            if current.data < mini:
                mini = current.data
            else:
                current = current.left
        return mini

    # Find the max node
    def find_max_node(self) -> int:
        if not self.root:
            return -1
        current = self.root
        max_n = self.root.data
        while current is not None:
            if current.data > max_n:
                max_n = current.data
            else:
                current = current.right
        return max_n

    # Delete a node
    def delete_node(self, val):
        if not self.root:
            return

        parent = None
        current = self.root

        # Step 1: Find the node to delete
        while current and current.data != val:
            parent = current
            if val < current.data:
                current = current.left
            else:
                current = current.right

        if current is None:
            return  # Node not found

        # Step 2: Node has two children
        if current.left and current.right:
            # Find inorder successor (smallest in right subtree)
            succ_parent = current
            successor = current.right
            while successor.left:
                succ_parent = successor
                successor = successor.left

            # Replace current's data with successor's data
            current.data = successor.data

            # Now delete successor node
            parent = succ_parent
            current = successor

        # Step 3: Node has one child or no child
        child = current.left if current.left else current.right

        if parent is None:
            # Deleting the root node
            self.root = child
        elif parent.left == current:
            parent.left = child
        else:
            parent.right = child


if __name__ == "__main__":
    bst = BinarySearchTree()
    # for i in [3, 2, 1, 4, 5, 6]:
    #     bst.insert(i)
    print("\n--------------- Insertion using recursion --------------------")
    for i in [3, 2, 1, 4, 5, 6, 0]:
        bst.root = bst.insertion_using_recursion(bst.root, i)
    print("\n--------------- Inorder with recursion --------------------")
    bst.inorder(bst.root)
    print("\n--------------- Search in the BST --------------------")
    res = bst.search(2)
    print(f"Value in bst: {res}")
    print("\n--------------- Find minimum in the BST --------------------")
    res = bst.find_min_node()
    print(f"Min in bst: {res}")
    print("\n--------------- Find maximum in the BST --------------------")
    res = bst.find_max_node()
    print(f"Max in bst: {res}")
    print("\n--------------- Remove element from BST --------------------")
    bst.delete_node(5)
    bst.inorder(bst.root)
