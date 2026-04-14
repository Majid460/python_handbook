# Trees - Sub type of graph with no cycles
# BST - Left child is smaller than right


from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Tree:

    def __init__(self):
        self.root: Node = None

    # Append
    # Use Queue to check at each level and then insert
    def append(self, data):
        new_node = Node(data)

        if not self.root:
            return new_node
        # init queue
        queue = deque([self.root])
        while queue:
            curr = queue.popleft()  # pop left element
            if not curr.left:
                curr.left = new_node
                return self.root
            # if left exist
            else:
                queue.append(curr.left)
            if not curr.right:
                curr.right = new_node
                return self.root
            # if left exist
            else:
                queue.append(curr.right)

    # traverse - inorder
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    # Pre - order
    def pre_order(self, node):
        if node:
            print(node.data, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)

    # Find the number
    # 1st using queue
    def find_number(self, target):
        if not self.root:
            return False
        queue = deque([self.root])
        while queue:
            curr = queue.popleft()
            if curr.data == target:
                return True
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return False

    # Find number using DFS
    def find_number_dfs(self, node: Node, target):
        if not node:
            return False
        if node.data == target:
            return True
        # Pass left and right
        return self.find_number_dfs(node.left, target) or self.find_number_dfs(
            node.right, target
        )


if __name__ == "__main__":
    print("here")
    tree = Tree()
    for i in (3, 2, 1, 4, 5, 6, 0):
        tree.root = tree.append(i)
    tree.inorder(tree.root)
    print("\n--- pre-order ----")
    tree.pre_order(tree.root)
    print("\n---- Find Number bfs -----")
    print(tree.find_number(6))
    print("\n---- Find Number dfs -----")
    print(tree.find_number_dfs(tree.root, 6))
