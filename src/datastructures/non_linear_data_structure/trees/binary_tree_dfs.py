from collections import deque
from inspect import stack


# Binary tree with DFS means using Stack

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class DfsTree:
    def __init__(self):
        self.root = None

    # Insertion using DFS
    def insert_in_tree(self, data):
        new_node = TreeNode(data)
        if not self.root:
            self.root = new_node
            return
        stack = deque([self.root])
        while stack:
            temp_node = stack.pop()
            if not temp_node.left:
                temp_node.left = new_node
                return
            elif not temp_node.right:
                temp_node.right = new_node
                return
            else:
                stack.append(temp_node.right)
                stack.append(temp_node.left)

    # Inorder with recursion
    def inorder(self, node: TreeNode):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    # Inorder without recursion using stack
    def inorder_without_recursion(self):
        if not self.root:
            return
        stack = []
        current = self.root

        while stack or current:
            # 1. Go all the way left
            while current:
                stack.append(current)
                current = current.left

            # 2. Process node
            current = stack.pop()
            print(current.data, end=" ")
            # 3. Go right
            current = current.right

    # Preorder with recursion
    def preorder(self, node: TreeNode):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # Preorder without recursion
    def preorder_without_recursion(self):
        if not self.root:
            return
        stack = [self.root]
        while stack:
            current = stack.pop()
            print(current.data, end=" ")
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)


if __name__ == '__main__':
    dfs = DfsTree()
    for i in [1, 2, 3, 4, 5, 6]:
        dfs.insert_in_tree(i)
    print("\n--------------- Inorder order --------------------")
    dfs.inorder(dfs.root)
    print("\n--------------- Inorder without recursion --------------------")
    dfs.inorder_without_recursion()
    print("\n--------------- Preorder with recursion --------------------")
    dfs.preorder(dfs.root)
    print("\n--------------- Preorder without recursion --------------------")
    dfs.preorder_without_recursion()
