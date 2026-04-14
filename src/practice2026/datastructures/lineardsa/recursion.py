from typing import List

"""
The One Mental Model That Makes Recursion Click
Most people think of recursion as a function calling itself. That's technically true but it's the wrong mental model. Here's the right one:

Recursion is believing that your function already works for a smaller problem, and using that belief to solve the bigger one.

Read that again. It's everything.

The 3-Part Structure — Every Recursive Function Ever Written
1. BASE CASE   → when do I stop?
2. TRUST       → assume the function works for n-1
3. BUILD       → use that result to solve for n
"""


def sum_list(arr: List[int]):

    # Base Case
    if not arr:
        return 0
    # Trust + Build
    # Trust: sum_list(arr[1:]) already works for smaller list
    # Build: add first element to that result
    return arr[0] + sum_list(arr[1:])


# Optimal solution with no slicing
def sum_list_op(arr, i=0):
    if i == len(arr):
        return 0
    print(arr[i], i, sum_list_op(arr, i + 1))
    return arr[i] + sum_list_op(arr, i + 1)


# Reverse a string "hello" -> olleh
def reverse(s: str):
    if len(s) <= 1:
        return s
    return reverse(s[1:]) + s[0]


# Power function
def power(base: int, exp: int):
    # Any number power 0 is 1
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


"""
if BASE_CASE:
    return SIMPLE_ANSWER

return COMBINE(current_element, recursive_call(smaller_problem))
power(2, 3)
= 2 * power(2, 2)
= 2 * (2 * power(2, 1))
= 2 * (2 * (2 * power(2, 0)))
= 2 * 2 * 2 * 1 = 8

"""

# print(sum_list_op([1, 2]))
print(reverse("hello"))
print(power(2, 2))
