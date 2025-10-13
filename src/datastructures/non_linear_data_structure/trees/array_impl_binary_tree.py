"""
Instead of using nodes (Node.left, Node.right), we represent a binary tree as a list (array).

Each node’s position in the array represents its position in the tree.

Relationships (parent ↔ children) are determined by index formulas:

Left child of index i → 2*i + 1
Right child of index i → 2*i + 2
Parent of index i → (i - 1) // 2

Why is it important?
Memory efficiency: No extra memory for Node objects and pointers.
Fast access: Accessing parent/child is O(1) (just index math).
Used in Heaps: Heap data structure (for Priority Queues, Heap Sort, Dijkstra, etc.) is implemented this way.
Cache-friendly: Arrays are stored in contiguous memory, which makes traversal faster in practice than pointer-based trees.
"""


class ArrayBinaryTree:
    def __init__(self, size):
        self.arr = [None] * size
        self.size = size
        self.last_index = -1

    # Insert in tree
    # Insert in level-order (like heap insertion)
    def insert(self, val):
        if self.last_index + 1 >= self.size:
            print("Tree is full")
            return
        self.last_index += 1
        self.arr[self.last_index] = val

    # display
    def display(self):
        print(self.arr[:self.last_index + 1])

    # Inorder traversal (recursive using indices)
    def inorder(self, i=0):
        if i > self.last_index or self.arr[i] is None:
            return
        # left -> root -> right
        self.inorder(2 * i + 1)
        print(self.arr[i], end=" ")
        self.inorder(2 * i + 2)

    # Get parent value of node at index i
    def get_parent(self, i=0):
        if i == 0:  # Root has no parent
            return None
        return self.arr[(i - 1) // 2]

    # Get left child value of node at index i
    def get_left(self, i=0):
        if i >= self.size or self.arr[i] is None:
            return None
        left_index = 2 * i + 1
        return self.arr[left_index]

    # Get left child value of node at index i
    def get_right(self, i=0):
        if i >= self.size or self.arr[i] is None:
            return None
        right_index = 2 * i + 2
        return self.arr[right_index]


if __name__ == '__main__':
    bt = ArrayBinaryTree(15)

    # Insert values
    for val in [10, 20, 30, 40, 50, 60]:
        bt.insert(val)

    bt.display()

    print("\nInorder Traversal:")
    bt.inorder()
    # Access specific relationships
    print("\n\nAccess examples:")
    print("Parent of index 4:", bt.get_parent(4))  # 20
    print("Left child of index 1:", bt.get_left(1))  # 40
    print("Right child of index 1:", bt.get_right(1))
