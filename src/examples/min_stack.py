"""
Problem:
Design a stack that supports:

- push(x)
- pop()
- top()
- getMin() → retrieves the minimum element in O(1) time

Hint: Use two stacks: one normal stack, one for storing current minimums.
"""
from collections import deque
from math import floor
from numbers import Integral


class MinStack:
    def __init__(self):
        self.normal_stack = []
        self.min_stack = []

    # Push into stack
    def push(self, val: int) -> bool:
        self.normal_stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        return True

    # Pop element (This is not optimal for optimal i need to has lookup with hashmap for both lists indexes)
    def pop(self) -> bool:
        if not self.normal_stack:
            return False
        val = self.normal_stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return True

    # top element
    def top_element(self) -> int:
        if len(self.normal_stack) == 0:
            return -1
        else:
            return self.normal_stack[-1]

    # Get minimum
    def get_minimum(self) -> int | bool:
        if not self.min_stack:
            return False
        else:
            return self.min_stack.pop()


if __name__ == '__main__':
    min_stack = MinStack()
    print("\n----------------- Push ----------------------")
    [print(min_stack.push(i)) for i in [3, 22, 1, 4, 8]]
    print(min_stack.normal_stack)
    [print(i, end=" ") for i in min_stack.min_stack]
    print("\n----------------- Pop ----------------------")
    res = min_stack.pop()
    print(f"Popped element => {res}")
    print("\n----------------- Get Min ----------------------")
    res = min_stack.get_minimum()
    if isinstance(res, Integral):
        print(f"Min value in stack: {res}")
    else:
        print("Stack is empty")
