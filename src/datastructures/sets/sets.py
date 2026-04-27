"""
Sets - Completely opposite of list
myset = {"apple", "banana", "cherry"}
- Sets are used to store multiple items in a single variable.
A set is a collection which is unordered, unchangeable, and unindexed with no duplicates allowed.

Note: Set items are unchangeable, but you can remove items and add new items.
"""

print("\n----------- Sets -------------\n")
my_set = {"apple", "banana", "cherry"}
print(f"Set => {my_set}")
# Set => {'banana', 'cherry', 'apple'}
print("\n----------- Set Operations -------------\n")
# 1. Duplicates are not allowed

my_set = {"apple", "banana", "cherry", "apple"}
print(f"Set after adding duplicate => {my_set}")
# Set => {'apple', 'banana', 'cherry'}

"""
Note:
The values True and 1 are considered the same value in sets, and are treated as duplicates:
- As in following example it removed the true and false from set and keep 0 means false, 1 means true
"""
my_set = {"apple", "banana", "cherry", 1, True, 0, False}
print(f"The set after adding true and 0 => {my_set}")
# The set after adding true and 0 => {0, 1, 'cherry', 'banana', 'apple'}

# 2. Length of set
print(f"Length of set is: {len(my_set)}")
# Length of set is: 5

# Set can have any datatype in it.
# A set with strings, integers and boolean values:
set1 = {"abc", 34, True, 40, "male"}

# 3. We can also create a set with set constructor
set2 = set(("A", "B", "C"))
print(set2)

# 4. Access Items from set
"""
First, remember: sets in Python are unordered,un-indexed collections of unique elements.
That means:
You can’t access elements by index (like in a list or tuple).
You can only iterate or check membership.
"""
# 1. Iterate on set
for element in set2:
    print(f"Element in set is: {element}")

"""
Element in set is: A
Element in set is: C
Element in set is: B
"""
# 2. Check membership
print("A" in set2)  # True
print("G" not in set2)  # True

print("\n----------- Set Immutability -------------\n")
"""
Once a set is created, you cannot change its items, but you can add new items.
- Once a set is created, you cannot change its items, but you can add new items.

"""
# 1. Add new item
# To add a new item in set just use add() method

set2.add("D")
print(f"Set after adding new value: {set2}")
# Set after adding new value: {'A', 'D', 'C', 'B'}

this_set = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

this_set.update(tropical)
print(f"Set after adding new set: {this_set}")
# Set after adding new set: {'apple', 'papaya', 'cherry', 'pineapple', 'banana', 'mango'}

# Add any iterable in set
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
this_set = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

this_set.update(mylist)
print(f"Set after adding new list: {this_set}")
# Set after adding new list: {'banana', 'cherry', 'orange', 'kiwi', 'apple'}

# 2. Remove an item from set
# To remove an item in a set, use the remove(), or the discard() method.

this_set.remove("apple")
print(f"Set after removing an object: {this_set}")
# Set after removing an object: {'cherry', 'orange', 'banana', 'kiwi'}
"""
Note: 
If the item to remove does not exist, remove() will raise an error.
"""
this_set.discard("kiwi")
print(f"Set after removing an object: {this_set}")
# Set after removing an object: {'orange', 'banana', 'cherry'}
"""
Note: If the item to remove does not exist, discard() will NOT raise an error.
"""

"""
You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
The return value of the pop() method is the removed item.
"""
this_set.pop()
print(f"Set after removing an object using pop: {this_set}")
# Set after removing an object using pop: {'banana', 'cherry'}
# Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

# The del keyword will delete the set completely:
del this_set

print("\n----------- Join Sets -------------\n")
"""
There are several ways to join two or more sets in Python.
- The union() and update() methods joins all items from both sets.
- The intersection() method keeps ONLY the duplicates.
- The difference() method keeps the items from the first set that are not in the other set(s).
- The symmetric_difference() method keeps all items EXCEPT the duplicates.
"""
print("\n-----------1. Union of Sets -------------\n")
# 1. Union
# Union() join will join all the items of sets
set_a = {"apple", "banana", "cherry"}
set_b = {"pineapple", "apple", "papaya"}
union = set_a.union(set_b)
print(f"Union of sets:=> {union}")
# Union of sets:=> {'banana', 'apple', 'mango', 'cherry', 'pineapple', 'papaya'}

# Union can also apply by update
set_a.update(set_b)
print(f"Union of sets by update :=> {set_a}")
# Union of sets by update :=> {'banana', 'pineapple', 'mango', 'papaya', 'cherry', 'apple'}

# Join can also work with | (OR) operator such as set_a | set_b

print("\n-----------2. Intersection of Sets -------------\n")
set_a = {"apple", "banana", "cherry"}
set_b = {"pineapple", "apple", "papaya"}
# Get common items from both
inter = set_a.intersection(set_b)
print(f"Intersection of sets :=> {inter}")
# Intersection of sets :=> {'apple'}

# For Intersection & operator you can also use it.
inter = set_a & set_b
print(f"Intersection of sets :=> {inter}")
# Intersection of sets :=> {'apple'}

print("\n-----------2. Difference of Sets -------------\n")
# In difference of sets, only get the values that are present in first set but not present in other sets.

diff = set_a.difference(set_b)
print(f"Difference of sets:: {diff}")
# Difference of sets:: {'cherry', 'banana'}

# We can also use minus (-) operator for that.
set3 = set_a - set_b
print(f"Difference of sets:: {set3}")
# Difference of sets:: {'cherry', 'banana'}
# Use the difference_update() method to keep the items that are not present in both sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)
print(f"Difference update =>{set1}")
# Difference update =>{'cherry', 'banana'}

print("\n-----------2. Symmetric Difference of Sets -------------\n")
# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set3 = set_a.symmetric_difference(set_b)
print(f"Symmetric Difference=> {set3}")
# Symmetric Difference=> {'papaya', 'cherry', 'banana', 'pineapple'}

# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.

set3 = set_a ^ set_b
print(set3)
# {'papaya', 'pineapple', 'cherry', 'banana'}
