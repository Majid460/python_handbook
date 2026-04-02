import math
from math import *


# Separate Numbers
# Reverse Numbers
# To count digits introduce a variable
def print_numbers(n: int):
    count = 0
    while n > 0:
        last_digit = n % 10
        count += 1
        print(f"{last_digit}", end=" ")
        n = n // 10
    print()
    print(f"digit counts:: {count}")


# Count Numbers using log
def count_integers(n: int):
    print(int(math.log10(n) + 1))


# Remove minimum parenthesis from string like (a(b)))
def remove_parenthesis(s: str):
    stack = []
    remove = set()

    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            if stack:
                stack.pop()
            else:
                remove.add(i)

    remove.update(stack)

    result = "".join(ch for i, ch in enumerate(s) if i not in remove)
    print(result)


if __name__ == '__main__':
    n1 = 4393
    print_numbers(n1)
    count_integers(n1)
    print("-------- Remove parenthesis----------")
    remove_parenthesis("()())()")
