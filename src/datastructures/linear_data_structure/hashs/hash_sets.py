"""
Hash Set

A Hash Set is a form of Hash Table data structure that usually holds a large number of elements.
Using a Hash Set we can search, add, and remove elements really fast.
Hash Sets are used for lookup, to check if an element is part of a set.
- It is used to store unique values in hash table
"""


class HashSet:
    def __init__(self, size):
        self.hash_set = [None for _ in range(size)]

    # Hash function
    def hash_function(self, val):
        match val:
            case str():
                return sum(ord(char) for char in val) % 10
            case int():
                return val % 10
            case _:
                return None

    def is_empty(self, inner_list: list):
        return len(inner_list) == 0

    # Add value in hash set
    def add(self, val):
        index = self.hash_function(val)
        # Case 1: Slot has no value
        if self.hash_set[index] is None:
            self.hash_set[index] = val
        # Case 2: Slot has a list
        if isinstance(self.hash_set[index], list):
            if val not in self.hash_set[index]:
                self.hash_set[index].append(val)
        # Case 3: Slot has no list but has value
        else:
            if val not in self.hash_set[index]:
                self.hash_set[index] = [self.hash_set[index], val]


if __name__ == "__main__":
    hash_set = HashSet(size=10)
    hash_set.add("Charlotte")
    hash_set.add("Thomas")
    hash_set.add("Jens")
    hash_set.add("Peter")
    hash_set.add("Lisa")
    hash_set.add("Adele")
    hash_set.add("Michaela")
    hash_set.add("Bob")
    hash_set.add("Alice")
    print(hash_set.hash_set)
