from typing import List

# Stack problems
# Stack -> Last in First out -> LIFO
# An array impl by default is stack
# You can only add to top
# You can only remove from top


def stack_basic():
    stack = []
    # Append new in stack
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    # Peek — look at top without removing
    top = stack[-1]  # 3
    print(top)
    # Check empty
    if not stack:
        print("empty")
    # Now remove element from stack which will by default remove from last
    stack.pop()  # Will remove last element
    stack.pop(1)  # Remove and return item at index (default last)
    # Pop op return the updated list after removing
    # stack.remove(2)  # Remove first occurrence of value.
    del stack[0]  # does not return any value
    print(stack)


# Before teaching the problem, wire the trigger:

# > **Anytime you need to remember something, then come back to it later in reverse order — that's a stack.**


# Stack Problems
# Prob 1 - Valid Parentheses — The Classic Stack Problem
# str = "({[]})" # check this string of parenthesis is valid or not?
def check_parentheses(s: str) -> bool:
    stack = []

    # Define map for Parentheses
    matching = {"}": "{", "]": "[", ")": "("}  # check the every closing has a opening
    for ch in s:  # for every char in string
        if ch in matching.values():  # Opening brackets e.g, '['
            stack.append(ch)
        elif ch in matching.keys():
            # Closing bracket — must match top of stack e.g, ']'
            if not stack:
                return False  # nothing to match
            # Remove the top inserted opening bracket
            top = stack.pop()
            if top != matching[ch]:
                return False  # wrong match

    return len(stack) == 0  # Only valid is nothing left in stack


# Track where the mismatch occur
from typing import List


def track_and_check_parentheses(s: str):
    stack: List = []
    invalid = []

    matching = {"}": "{", "]": "[", ")": "("}

    for i, ch in enumerate(s):
        if ch in matching.values():  # opening
            stack.append((ch, i))

        elif ch in matching:  # closing
            if not stack:
                invalid.append(i)
                continue

            top_bracket, top_index = stack.pop()

            if top_bracket != matching[ch]:
                invalid.append(i)
                invalid.append(top_index)  # also mark opening as invalid

    # remaining unclosed openings
    while stack:
        _, idx = stack.pop()
        invalid.append(idx)

    if not invalid:
        return -1

    return sorted(invalid)


# You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.
# Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.


def temp_finder(arr: List[int]):
    # Use stack which will be monotonic decreasing stack
    stack = []
    n = len(arr)
    answer = [0] * n

    for i, temp in enumerate(arr):
        # check in stack for each iteration the value on top is greater or less
        while (
            stack and temp > arr[stack[-1]]
        ):  # -1 -> last temp on stack and 0 -> temp is first value
            # if yes -> pop the values
            stack_index = stack.pop()
            answer[stack_index] = i - stack_index
        stack.append(i)

    return answer


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)
    stack = []  # pair: [temp, index]

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = i - stackInd
        stack.append((t, i))
    return res


if __name__ == "__main__":
    # stack_basic()
    s = "({(}"
    # print(f"Are paranthes valid: {check_parentheses(s)}")
    # print(f"Are paranthes valid: {track_and_check_parentheses(s)}")
    val = track_and_check_parentheses(s)

    if isinstance(val, int):
        print(f"Parentheses are valid")

    elif isinstance(val, list):
        for idx in val:
            print(f"Invalid at index {idx}")

    # Temp
    print("Prob - temp")
    print(temp_finder([73, 74, 75, 71, 69, 72, 76, 73]))
