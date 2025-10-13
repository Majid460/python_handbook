"""
Design a class:

- Inserting a value (no duplicates)
- Removing a value
- GetRandom a value that is already inserted (with equal probability)

All functions must run in average O(1) time.

We use two structures together:

List/Array → to store values (so we can get random element in O(1)).
HashMap (dict) → to store each value’s index in the list (so we can insert/remove in O(1)).

Because if we try to delete to remove element from list it will cost O(n) because it will shift all elements
"""
from random import Random


class StoreData:
    def __init__(self):
        self.arr = []
        self.hash_map = {}
    # Insert value
    def insert(self,val) -> bool:
        # To check duplicates
        if val in self.hash_map:
            return False
        self.arr.append(val)
        self.hash_map[val] = len(self.arr) - 1
        return True
    # Remove elements with O(1)
    def remove(self,val:int) -> bool:
        # To check if val is not in hashmap
        if val not in self.hash_map:
            return False
        # Find index of element to be remove from the hashmap
        idx = self.hash_map.get(val)
        # Find the element and swap to last
        element = self.arr[idx]
        # Get last element
        last = self.arr[-1]
        # Swap the removing element with last
        self.arr[idx] = last
        self.arr[-1] = element

        # Remove last from list and also from hashmap
        self.arr.pop()
        self.hash_map.pop(val)

        return True

    # Get random value on equal probability
    def random_removal(self) -> int:
        return Random.choice(Random(),seq=self.arr)

if __name__ == '__main__':
    store = StoreData()
    print("\n----------------- Insert ----------------------")
    [print(store.insert(i)) for i in [1,2,1,3,4]]
    print("\n----------------- Remove ----------------------")
    res = store.remove(3)
    print(res)
    print("\n----------------- Remove at random ----------------------")
    res1 = store.random_removal()
    print(res1)


