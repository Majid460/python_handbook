from collections import deque
from typing import List
from enum import Enum

"""
| Type                 | Condition                      |
| -------------------- | ------------------------------ |
| Full Binary Tree     | Every node has 0 or 2 children |
| Perfect Binary Tree  | All levels completely filled   |
| Complete Binary Tree | Last level filled left → right |

"""


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class ViewType(Enum):
    RIGHT = 1
    LEFT = 2


# Left always less than right
class Bst:
    def __init__(self) -> None:
        self.root: Node = None

    def append(self, data):
        new_node = Node(data)
        # check if root exists
        if not self.root:
            self.root = new_node
            return
        # if yes -> then make a curr pointer point to root
        curr = self.root

        # loop until found a space to insert
        while True:
            if new_node.data > curr.data:
                if not curr.right:
                    curr.right = new_node
                    break
                curr = curr.right
            else:
                if not curr.left:
                    curr.left = new_node
                    break
                curr = curr.left

    # Pre - order
    def pre_order(self, node):
        if node:
            print(node.data, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)

    # Search in bst
    def search_bst(self, target):
        if not self.root:
            return False
        curr = self.root
        while curr:
            if curr.data == target:
                return True
            elif target > curr.data:
                curr = curr.right
            elif target < curr.data:
                curr = curr.left
        return False

    # Find Min node
    def find_min_node(self):
        if not self.root:
            return False
        min_n = self.root.data
        curr = self.root
        while curr:
            if curr.data < min_n:
                min_n = curr.data
            curr = curr.left

        return min_n

    # Find the max node
    def find_max_node(self):
        if not self.root:
            return
        curr = self.root
        max_n = curr.data
        while curr:
            max_n = max(curr.data, max_n)
            curr = curr.right
        return max_n

    # Find max using recursion
    def find_max_rec(self, node):
        if not node:
            return float("-inf")
        right = self.find_max_rec(node.right)
        return max(node.data, right)

    # Find sum of left side dfs
    def sum_tree(self, node):
        if not node:
            return 0
        return node.data + self.sum_tree(node.left) + self.sum_tree(node.right)

    # Find sum of right sub tree
    # Find sum of left sub tree
    def sum_of_sides_of_tree(self, root, view_type: ViewType):
        if not root:
            return 0

        child = root.left if view_type == ViewType.LEFT else root.right
        return self.sum_tree(child) if child else 0

    # Find sum of whole tree dfs
    def sum_of_tree(self, node):
        if not node:
            return 0
        left = self.sum_of_tree(node.left)
        right = self.sum_of_tree(node.right)
        return node.data + left + right

    def delete(self, node, target):
        # In recursion, deleting a node is just returning what should replace it.
        # Base case
        if not node:
            return node
        # Navigate to the node
        if target < node.data:
            node.left = self.delete(node.left, target)
        elif target > node.data:
            node.right = self.delete(node.right, target)
        else:
            # FOUND IT — handle 3 cases here

            if not node.left:
                return node.right  # covers leaf + right child

            if not node.right:
                return node.left  # covers leaf + left child

            # For leaf
            # node.left = None
            # node.right = None

            # Case 3: two children
            # Replace the value with the smallest value on right sub tree
            successor = node.right
            while successor.left:
                successor = successor.left
            # Step 2: replace value
            node.data = successor.data
            # Step 3: delete successor node
            node.right = self.delete(node.right, successor.data)

        return node

    # Level wise traversing
    # Using bfs
    def level_traverse(self):
        if not self.root:
            return
        queue = deque([self.root])
        level: int = 0
        result = []
        # Load each level in the queue and check size and append in level list
        while queue:
            queue_size = len(queue)

            levels = []  # to hold each level
            for _ in range(queue_size):
                curr = queue.popleft()
                levels.append(curr.data)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            print(f"At Level: {level} : {levels}")
            level += 1
            result.append(levels)
        return result

    def sum_of_path(self, node: Node, target: int):
        if not node:
            return False

        if not node.left and not node.right:
            return target == node.data

        return self.sum_of_path(node.left, target - node.data) or self.sum_of_path(
            node.right, target - node.data
        )

    # Using BFS
    def sum_of_path_using_bfs(self, target: int):
        if not self.root:
            return False
        queue = deque([(self.root, target - self.root.data)])  # root and remaining
        while queue:
            curr, remaining = queue.popleft()

            # check if leaf
            if not curr.left and not curr.right and remaining == 0:
                return True
            if curr.left:
                queue.append((curr.left, remaining - curr.left.data))
            if curr.right:
                queue.append((curr.right, remaining - curr.right.data))

        return False

    # Invert the BST using BFS

    # Left view using BFS AND Right view
    def view(self, view_type: ViewType) -> List[int]:
        queue = deque([self.root])
        view = []
        # Load each level in the queue and check size and append in level list
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()

                if (view_type == ViewType.RIGHT and i == size - 1) or (
                    view_type == ViewType.LEFT and i == 0
                ):
                    # For left take first element
                    # For Right - [n1,n2] -> take n2 so : i==1 and size-1 = 1 take right
                    # Only add the last node of each level
                    view.append(curr.data)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return view

    def right_view(self):
        if not self.root:
            return []
        return self.view(ViewType.RIGHT)

    def left_view(self):
        if not self.root:
            return []
        return self.view(ViewType.LEFT)

    # Check if two trees are identical → BFS or DFS?
    # Using bfs
    def is_same_tree(self, tree_a: Node, tree_b: Node):
        if not tree_a and not tree_b:
            return True
        if not tree_a or not tree_b:
            return False

        queue = deque([(tree_a, tree_b)])

        while queue:
            n1, n2 = queue.popleft()

            if not n1 and not n2:
                continue
            if not n1 or not n2:
                return False
            if n1.data != n2.data:
                return False

            queue.append((n1.left, n2.left))
            queue.append((n1.right, n2.right))

        return True

    # ----- Recursion ------

    # Height of BST - The maximum depth or height of the tree is the number of edges in the tree from the root to the deepest node.
    # Using DFS
    def max_height(self, node: Node):
        # If we are counting height based on edges we need to return -1 for leaf nodes to balance result
        if not node:
            return -1
        left = self.max_height(node.left)
        right = self.max_height(node.right)
        return 1 + max(left, right)  # 1+ -> It represents the edge (or level increment)

    # Print the right nodes
    def right_nodes(self, root: Node):
        if not root:
            return []
        if not root.right:
            return [root.data]
        return [root.data] + self.right_nodes(root.right)

    def rightSideView(root):
        res = []

        def dfs(node, depth):
            if not node:
                return

            # First node we visit at this depth
            if depth == len(res):
                res.append(node.val)

            # Go right first
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res

    # Count nodes
    def count_nodes(self, node: Node):
        if not node:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    # Check value exists in tree
    def has_value(self, node, val):
        """
        If node is None → False
        If node matches → True
        Search left OR right
        """
        if not node:
            return False
        if node.data == val:
            return True
        return self.has_value(node.left, val) or self.has_value(node.right, node.val)

    # Check if a tree is symmetric
    """
    A tree is symmetric if:

    Left subtree is a mirror image of the right subtree
    e.g: 
        1
       / \
      2   2
     / \ / \
    3  4 4  3
    """

    def is_mirror(self, node):
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.data != right.data:
                return False
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        if not node:
            return True
        return dfs(node.left, node.right)

    # Diamter of BST
    # Longest path on left + longest path on right
    def diameter(self, node):
        # Member variable of the instance of this class which will be accessible inside the inner function
        self.res = 0

        # Return the height of sub trees
        def dfs(node):
            if not node:
                return 0
            # Height of left subtree
            left = self.diameter(node.left)
            right = self.diameter(node.right)
            # Max this result
            self.res = max(self.res, left + right)
            return 1 + max(left, right)  # Height

        dfs(node)
        return self.res

    # Check complete tree


if __name__ == "__main__":
    bst = Bst()
    for i in (3, 2, 1, 4, 5, 6, 0):
        bst.append(i)
    """
        3
       / \
      2   4
     /     \
    1       5
   /         \
  0           6
"""

    print("\n---- BST Insert ---- ")
    bst.pre_order(bst.root)

    print("\n---- BST Search ---- ")
    print(bst.search_bst(9))

    print("\n---- BST Min node ---- ")
    print(bst.find_min_node())

    print("\n---- BST Max node ---- ")
    print(bst.find_max_node())
    print(bst.find_max_rec(bst.root))

    print("\n---- BST sum of left sub tree ---- ")
    print(bst.sum_of_sides_of_tree(bst.root, ViewType.LEFT))

    print("\n---- BST sum of right sub tree ---- ")
    print(bst.sum_of_sides_of_tree(bst.root, ViewType.RIGHT))

    print("\n---- BST sum of whole tree ---- ")
    print(bst.sum_of_tree(bst.root))

    # print("\n---- Delete in BST ---- ")
    # bst.delete(bst.root, 2)
    # bst.pre_order(bst.root)

    print("\n---- Level traverse in BST ---- ")
    bst.level_traverse()

    print("\n---- Max Height in BST ---- ")
    print(bst.max_height(bst.root))

    print("\n---- Sum of path in BST ---- ")
    print(bst.sum_of_path(bst.root, target=6))
    print(bst.sum_of_path_using_bfs(target=6))

    print("\n---- Left view of BST ---- ")
    rs = bst.left_view()
    [print(f"{v}", end="-> " if i != len(rs) - 1 else " ") for i, v in enumerate(rs)]

    print("\n---- Right view of BST ---- ")
    rs = bst.right_view()
    [print(f"{v}", end="-> " if i != len(rs) - 1 else " ") for i, v in enumerate(rs)]

    print("\n------ Right Nodes ------")
    print(bst.right_nodes(bst.root))

    print("\n------ Count Nodes ------")
    print(bst.count_nodes(bst.root))

    print("\n------ Has Value in tree  ------")
    print(bst.has_value(bst.root, 0))

    print("\n------ Diameter tree  ------")
    print(bst.diameter(bst.root))
