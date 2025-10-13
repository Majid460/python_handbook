# Binary Tree Simple implementation
# The Binary Tree above can be implemented much like we implemented a Singly Linked List, except that instead of linking each node to one next node, we create a structure where each node can be linked to both its left and right child nodes.
from collections import deque

# For depth first search -> PreOrder, PostOrder, InOrder traversal used
# For breadth first search -> Level insertion with queue used

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Simple tree without level based insertion
class BinaryTree:
    def __init__(self, root=None):
        if root:
            self.root = TreeNode(root)
        else:
            self.root = None

    # For insertion in tree
    def insert(self, data):
        new_node = TreeNode(data)
        if not self.root:
            self.root = new_node
            return
        self.insert_recursive(self.root, new_node)

    def insert_recursive(self, current, new_node):
        # Try to insert in left subtree
        if not current.left:
            current.left = new_node
        elif not current.right:
            current.right = new_node
        else:
            # If both children exist → go left first
            self.insert_recursive(current.left, new_node)

    # Inorder Traversal (Left → Root → Right)
    def inorder_traversal(self, node: TreeNode):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

    # Preorder Traversal (Root, Left, Right)
    def preorder_traversal(self, node: TreeNode):
        if node:
            print(node.data, end=" ")
            self.inorder_traversal(node.left)
            self.inorder_traversal(node.right)

    # Postorder Traversal (Left, Right, Root)
    def postorder_traversal(self, node: TreeNode):
        if node:
            self.inorder_traversal(node.left)
            self.inorder_traversal(node.right)
            print(node.data, end=" ")


# Tree with level based insertion (Queue is used to fill levels) BFS
class BinaryLevelTree:
    def __init__(self):
        self.root = None

    # Insert using queue
    def insert_using_queue(self, data):
        new_node = TreeNode(data)
        if not self.root:
            self.root = new_node
            return
        queue = deque([self.root])
        while queue:
            temp = queue.popleft()
            if not temp.left:
                temp.left = new_node
                return
            else:
                queue.append(temp.left)
            if not temp.right:
                temp.right = new_node
                return
            else:
                queue.append(temp.right)

    # Level order traversal (BFS)
    def level_order(self):
        if not self.root:
            return
        queue = deque([self.root])
        while queue:
            node: TreeNode = queue.popleft()
            print(node.data, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    # Print levels of tree
    def print_levels(self):
        if not self.root:
            return
        queue = deque([self.root])
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node: TreeNode = queue.popleft()
                print(node.data, end=" ")
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print()

    # Count number of nodes
    def count_nodes(self):
        if not self.root:
            return
        queue = deque([self.root])
        count = {}
        level = 0

        while queue:
            level_size = len(queue)
            count[level] = level_size
            print(" Queue before pop:", [n.data for n in queue])
            for i in range(level_size):  # i represent each level
                node: TreeNode = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1

        return count

    # Find Maximum value in the tree
    def max_value(self):
        if not self.root:
            return
        maximum = -1
        queue = deque([self.root])
        while queue:
            temp_node: TreeNode = queue.popleft()
            if temp_node.data > maximum:
                maximum = temp_node.data
            if temp_node.left:
                queue.append(temp_node.left)
            if temp_node.right:
                queue.append(temp_node.right)
        return maximum

    # Height of tree
    def calc_height(self):
        if not self.root:
            return
        queue = deque([self.root])
        height = 0
        while queue:
            level_size = len(queue)
            for i in range(level_size):  # i represent each level
                node: TreeNode = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            height += 1
        return height

    # Search for a value in tree (Use BFS to find if a given value exists in the tree)
    def search_value(self, value):
        if not self.root:
            return
        queue = deque([self.root])
        while queue:
            temp_node = queue.popleft()
            if temp_node.data == value:
                return value
            if temp_node.left:
                queue.append(temp_node.left)
            if temp_node.right:
                queue.append(temp_node.right)
        return None

    # Print Left view of tree (First element at each level)
    def left_view(self):
        if not self.root:
            return
        queue = deque([self.root])
        left_view = []
        while queue:
            queue_size = len(queue)
            for i in range(queue_size):  # loop at each level
                node: TreeNode = queue.popleft()
                if i == 0:
                    left_view.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return left_view

    # Print right view of tree (last element at each level)
    def right_view(self):
        if not self.root:
            return
        queue = deque([self.root])
        right_view = []
        while queue:
            queue_size = len(queue)
            for i in range(queue_size):  # loop at each level
                node: TreeNode = queue.popleft()
                if i == queue_size - 1:
                    right_view.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return right_view

    # Print the left or right tree view
    def left_or_right(self, view_type: str):
        if not self.root:
            return
        queue = deque([self.root])
        view = []
        while queue:
            queue_size = len(queue)
            for i in range(queue_size):  # loop at each level
                node: TreeNode = queue.popleft()
                if view_type.__eq__("left") :
                    if i == 0:
                        view.append(node.data)
                if view_type.__eq__("right"):
                    if i == queue_size - 1:
                        view.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return view

    # Print level with Maximum sum
    def level_with_max_sum(self) -> tuple[int,int]:
        if not self.root:
            return -1,-1
        queue = deque([self.root])
        max_sum_total = float("-inf")
        max_level = -1
        level = 0
        while queue:
            sum_of_level = 0
            queue_size = len(queue)
            for i in range(queue_size): # each level
                temp_node = queue.popleft()
                sum_of_level += temp_node.data
                if temp_node.left:
                    queue.append(temp_node.left)
                if temp_node.right:
                    queue.append(temp_node.right)
            # check after finishing the level
            if sum_of_level > max_sum_total:
                    max_sum_total = sum_of_level
                    max_level = level
            level +=1
        return max_sum_total, max_level





if __name__ == '__main__':
    print("\n--------------- Simple tree without queue --------------------")
    bt = BinaryTree()
    for val in [1, 2, 3, 4, 5, 6]:
        bt.insert(val)
    print("\n--------------- Inorder --------------------")
    bt.inorder_traversal(bt.root)
    print("\n--------------- Preorder --------------------")
    bt.preorder_traversal(bt.root)
    print("\n--------------- Postorder --------------------")
    bt.postorder_traversal(bt.root)

    print("\n--------------- Binary tree with queue (BFS)--------------------")
    bl = BinaryLevelTree()
    for val in [1, 2, 3, 4, 5, 6]:
        bl.insert_using_queue(val)
    print("\n--------------- level order --------------------")
    bl.level_order()
    print("\n--------------- Print by level --------------------")
    bl.print_levels()
    print("\n--------------- Count nodes --------------------")
    res = bl.count_nodes()
    print(res)
    print("\n--------------- Maximum value --------------------")
    res = bl.max_value()
    print(f"Maximum value: {res}")
    print("\n--------------- Height of tree --------------------")
    res = bl.calc_height()
    print(f"Height of tree: {res}")
    print("\n--------------- Search value --------------------")
    res = bl.search_value(3)
    if res is not None:
        print(f"Value in tree found: {res}")
    else:
        print("Value not found")

    print("\n--------------- Left tree view --------------------")
    res = bl.left_view()
    [print(i) for i in res]
    print("\n--------------- Right tree view --------------------")
    res = bl.right_view()
    [print(i) for i in res]
    print("\n--------------- Left or Right tree view --------------------")
    print("\n ---- Left view ------")
    res = bl.left_or_right("left")
    [print(i) for i in res]
    print("\n ---- Right view ------")
    res = bl.left_or_right("right")
    [print(i) for i in res]

    print("\n--------------- Print level with Maximum sum  --------------------")
    max_sum, level = bl.level_with_max_sum()
    print(f"Max sum of level : {max_sum} and level {level}")

