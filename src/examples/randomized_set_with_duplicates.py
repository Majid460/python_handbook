"""
Problem:
Design a data structure that allows:
insert(val) → can insert duplicates
remove(val) → remove one occurrence of val
getRandom() → return random element all elements equally likely

all operations should be done in O(1)

Hint: Similar to your problem, but now you need a dict of val → set of indices because duplicates exist.
"""
import random


class RandSetDict:
    def __init__(self):
        self.arr = []
        self.hash_map = {}

    # Insert values in array and store values indices in the dict
    def insert(self, val: int) -> bool:
        # Insert value in the array
        self.arr.append(val)
        # Get the index of val inserted
        ind_x = len(self.arr) - 1
        # Check if value don't exist in the map insert it
        if val not in self.hash_map:
            self.hash_map[val] = {ind_x}
        # Check if value already exist then insert second index of value to handle duplicate
        else:
            self.hash_map[val].add(ind_x)
        return True

    # Remove the one occurrence of value
    def remove(self, val) -> int:
        if val not in self.hash_map or not self.hash_map[val]:
            return False
        ind_x = self.hash_map.get(val).pop()
        last_val = self.arr[-1]
        # Swap only if not removing the last element
        if ind_x != len(self.arr) - 1:
            temp = self.arr[ind_x]
            self.arr[ind_x] = last_val
            self.arr[-1] = temp
            # Update hashmap of last value
            self.hash_map[last_val].remove(len(self.arr) - 1)
            self.hash_map[last_val].add(ind_x)
        # Get value's index from hashmap
        removed = self.arr.pop()
        if not self.hash_map[val]:
            del self.hash_map[val]
        return removed

    # Get Random
    def random(self):
        return random.choice(self.arr)


if __name__ == '__main__':
    rand = RandSetDict()
    [rand.insert(i) for i in [1, 2, 4, 3, 2]]
    print("\n--------------Remove----------------")
    res = rand.remove(2)
    if res != -1: print(f"{res} has been removed")
    print(f"map::{rand.hash_map}")
    print(f"array: {rand.arr}")
    print("\n--------------Random----------------")
    res = rand.random()
    print(f"Random value::{res}")
