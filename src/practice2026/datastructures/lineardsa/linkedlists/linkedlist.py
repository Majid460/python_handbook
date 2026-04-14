# What Is a Linked List?
# Array is a row of lockers — fixed positions, side by side in memory.
# Linked list is a treasure hunt — each item holds the value AND a pointer to where the next item is.
# Array:
# [1, 2, 3, 4, 5]   ← all sitting together in memory, shoulder to shoulder

# Linked List:
# [1|→]  [2|→]  [3|→]  [4|→]  [5|→null]
#   ↑      ↑      ↑      ↑      ↑
#   scattered anywhere in memory, connected by pointers

# Each box is called a Node and contains two things:

# The value
# A pointer to the next node

# Benefits:
# 1. Frequent Insertions/Deletions at the Front O(n) - Just change the head
# 2. You Don't Know the Size in Advance
# 3. Splicing — Merging or Splitting Lists
# Split a linked list in half:
# Find middle → point middle.next = null → done. O(1) at the split point.

# Split an array in half:
# Must copy elements into two new arrays. O(n).


# Linked list Implementation:
class Node:
    def __init__(self, val=0):
        self.data = val
        self.next = None  # pointer to next node
        self.prev = None  # only for the doubly linked list


class LindedList:
    # Declear just head
    def __init__(self) -> None:
        self.head = None

    def add_node(self, val):
        # Add to end
        new_node = Node(val)

        if not self.head:
            # If there is no head exists, this node will be head
            self.head = new_node
            return
        # Else -> Create a pointer current, point to head and move to find end
        current = self.head
        while current.next:  # traverse to last node
            current = current.next
        current.next = new_node  # point last node to new

    def prepand(self, val):
        # Append at the start
        new_node = Node(val)
        # Always point this node next to head first
        new_node.next = self.head
        # New node is now pointing to old head node
        # Now change the head to new
        self.head = new_node

    def display(self):
        if not self.head:
            return
        current = self.head
        while current:
            # print(
            #     f"Current Node at: {id(current)},Node: {current.data} ,Next -> {current.next} "
            # )
            print(current.data, end=" → " if current.next != None else "")
            current = current.next
        print()

    def delete_node(self, val):
        # Check the head
        if not self.head:
            return
        # Special case — deleting head
        if self.head.data == val:
            self.head = self.head.next  # Point the head to the next node of first one
            return

        # Point current to same node head is pointing
        current = self.head
        while current.next:
            if current.next.data == val:
                current.next = current.next.next  # skip over it
                return
            current = current.next

    # Reverse the linked list
    def reverse(self):
        if not self.head:
            return
        # Use three pointers
        curr, prev = self.head, None
        print(f"prev:: {prev},current data::{curr.data}")
        while curr:
            next_n = curr.next  # store next node
            curr.next = prev  # reverse the link : curr->next -> prev
            prev = curr  # move prev forward : prev points to curr
            curr = next_n  # move current forward : curr points to next

        self.head = prev
        if not self.head:
            return
        current = self.head
        while current:
            print(current.data, end=" → " if current.next != None else "")
            current = current.next

    # Start:
    # prev=None  curr=1 → 2 → 3 → None

    # Step 1:
    # next_n=2
    # 1 → None  (reversed)
    # prev=1, curr=2

    # Step 2:
    # next_n=3
    # 2 → 1 → None
    # prev=2, curr=3

    # Step 3:
    # next_n=None
    # 3 → 2 → 1 → None
    # prev=3, curr=None

    # Exit loop:
    # self.head = prev = 3  ✓
    # Merge two sorted linked lists
    def merge_two_linked_list(self, list1: Node, list2: Node):
        dummy = Node()
        current = dummy

        while list1 and list2:
            if list1.data < list2.data:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        # Attach remaining nodes
        current.next = list1 if list1 else list2

        return dummy.next

    # Check the cycle exists
    def check_cycle_exist(self, head: Node):
        seen = set()
        curr = head
        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False

    # Remove second last element from list:
    def remove_second_last_element(self, head: Node):
        if not head:
            return
        curr = head
        while curr.next.next.next:  # curr|next -> next -> next -> None
            curr = curr.next
        # current.next is second last → delete it
        curr.next = curr.next.next
        return head

    # Remove the element from middle
    def remove_from_middle(self, target):
        if not self.head:
            return
        if target == self.head.data:  # If the deleting element is the head
            return self.head.next  # Point the head to the next element of head
        # If in middle
        prev, curr = self.head, self.head.next
        while curr:
            if target == curr.data:
                prev.next = curr.next  # point the previous to next of curr
                return self.head
            prev = curr
            curr = curr.next
        return self.head

    # Remove the nth element from list
    def remove_nth_element(self, head: Node, n):
        # Needs a pointer to hold the ref for head
        dummy = head
        # Create two pointers fast and slow
        # fast will move nth step ahead from slow
        slow = fast = dummy
        for _ in range(n):
            fast = fast.next
        # Move both until fast reaches last
        while fast.next:
            fast = fast.next
            slow = slow.next
        # Delete the nth node
        # slow is right behind the nth node, point it to the next of it next
        slow.next = slow.next.next
        return dummy

    # Time: O(n)
    # Space: O(1)

    def display_with_head(self, head: Node):
        if not head:
            return
        current = head
        while current:
            # print(
            #     f"Current Node at: {id(current)},Node: {current.data} ,Next -> {current.next} "
            # )
            print(current.data, end=" → " if current.next != None else "")
            current = current.next


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None

    def append(self, val):
        pass

    def display(self):
        pass


if __name__ == "__main__":

    # Singly
    print(
        "\n---------------------- Singly Linked List------------------------", end="\n"
    )
    linkList = LindedList()
    linkList.add_node(1)
    linkList.add_node(2)
    linkList.add_node(3)
    # linkList.prepand(0)
    linkList.display()
    # linkList.delete_node(2)
    # linkList.remove_from_middle(2)
    # print("\nAfter Deleting the node 2")
    # linkList.display()  # 1 → 3
    print("Reverse")
    linkList.reverse()

    print("\n--- Merged linked lists ---")
    # List 1: 1 -> 3 -> 5
    l1 = Node(1)
    l1.next = Node(3)
    l1.next.next = Node(5)
    l1.next.next.next = Node(3)

    # List 2: 2 -> 4 -> 6
    l2 = Node(2)
    l2.next = Node(4)
    l2.next.next = Node(6)

    merged = linkList.merge_two_linked_list(l1, l2)

    # Print result
    curr = merged
    while curr:
        print(curr.data, end=" → " if curr.next else "")
        curr = curr.next
    print()
    print(" ---- Check the cycle exists --- ")
    print(linkList.check_cycle_exist(l1))

    print("Remove the second last element")
    h = linkList.remove_second_last_element(l1)
    linkList.display_with_head(h)

    print("\n--- Remove the nth node ---")
    d = linkList.remove_nth_element(l1, 2)
    linkList.display_with_head(d)
