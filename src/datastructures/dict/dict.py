"""
Dictionary
- It is used to store key-value pairs
- A dictionary is a collection which is changeable, ordered, and don't allow duplicates
- The basic template of list is:
     dict = {
     "a":"AA",
     1:"1",
     }
Defined using curly braces {}.
Each item is a key: value pair.
Keys must be unique and immutable (strings, numbers, tuples).
Values can be of any type (string, list, object, even another dictionary).
"""

from typing import Dict


print("\n----------- Dictionaries -------------\n")
# To create an empty dictionary just use empty braces {}
dictionary = {}

# Dictionary with elements
d = {"A": "AA", "B": "BB"}

# Dictionary with constructor (Create with round braces())
d_con = dict([("A", "AA"), ("C", "BB")])
print(d_con)

# Get Values from the Dict
# 1. Simple with key
print(f"Element of dict at d['A']=> {d['A']}")
# Prints -> AA

# 2. whole dict
print(f"Elements of dict=> {d}")
# Elements of dict=> {'A': 'AA', 'B': 'BB'}

# 3. Using List
print(f"keys of dict using list => {list(d)}")
# keys of dict using list => ['A', 'B']

# 4. Using Sorted method
print(f"keys of dict using sorted method => {sorted(d)}")
# keys of dict using sorted method => ['A', 'B']

# 5. Using loop
for key in d:
    print(f"{key}=> {d[key]}")
"""
print:
A=> AA
B=> BB
"""
for value in d:
    print(f"{value}=> {d[value]}")
"""
print:
A=> AA
B=> BB
"""
for k, v in d.items():
    print(f"{k}=> {v}")
"""
A=> AA
B=> BB
"""
# To get index while looping through dictionary
for i, k in enumerate(d):
    print(f"{i}=> {k}")
"""
0=> A
1=> B
"""
# To loop over more than one sequences at a time
for a, b in zip(d, d_con):
    print(f"Zip of two dictionaries=> {a}=> {b}")
# 6. Dictionary using comprehension method
di = {x: x * 2 for x in (2, 4, 6)}
print(f"Dict using comprehension method => {di}")
# Dict using comprehension method => {2: 4, 4: 8, 6: 12}

# 7. Ordered (Dictionaries are ordered)
"""
How ordering works:
The order is based on when a key was first inserted.
Updating the value of an existing key does not change its position.
"""
"""
The order is based on when a key was first inserted.
Updating the value of an existing key does not change its position.
"""
d = {"x": 1, "y": 2, "z": 3}
print(list(d.keys()))
# ['x', 'y', 'z']
d["y"] = 100
print(list(d.keys()))
# ['x', 'y', 'z']

# But if you delete and reinsert a key, it moves to the end:
d = {"x": 1, "y": 2, "z": 3}
print(list(d.keys()))
# ['x', 'y', 'z']
del d["y"]
d["y"] = 200
print(list(d.keys()))
# ['x', 'z', 'y']

# 8. Update Method
# Update function can be used to add a new pair in the end of existing dict
d.update({"a": 12})
print(d)
# {'x': 1, 'z': 3, 'y': 200}
# {'x': 1, 'z': 3, 'y': 200, 'a': 12}

"""
 9. Remove elements
 To remove a certain element from the dictionary use pop(key) method
"""
d.pop("a")
print(f"Pop [a] from dict => [{d}")
# Pop [a] from dict => [{'x': 1, 'z': 3, 'y': 200}

# To pop last element from the dictionary use popitem()
d.popitem()
print(f"Pop last element from dict => [{d}")
# Pop last element from dict => [{'x': 1, 'z': 3}

# To remove a certain pair from the dict we can also use del
del d["z"]
print(f"Delete z key pair from dict => [{d}")
# Delete z key pair from dict => [{'x': 1}

# To make the dictionary empty
d.clear()
print(f"Delete all keys from dict => {d}")
# To delete the dictionary completely
del d

"""
To make copy of dictionary
- We can't just make a copy of the dict using equal sign. By 
- doing this it would not make copy of it but it will refer
- it to the same memory of first one. (Shallow copy)

- To make a copy just use copy function or use dict()
"""
d = {"a": 1, "b": 2, "c": 3}

d_copy = d

print(f"Memory address of first dictionary => {id(d)}")
print(f"Memory address of second dictionary => {id(d_copy)}")

"""
-- Same memory address
Memory address of first dictionary => 4313021312
Memory address of second dictionary => 4313021312
"""

# By the help of copy function we can make a deep copy
d_copy = d.copy()
print(f"Memory address of first dictionary => {id(d)}")
print(f"Memory address of second dictionary => {id(d_copy)}")
"""
-- By the help of copy function it changed the location of 
Memory address of first dictionary => 4341939072
Memory address of second dictionary => 4344170304
"""
# With dictionary, we can also create a deep copy
d_copy = dict(d)

print(f"Memory address of first dictionary => {id(d)}")
print(f"Memory address of second dictionary => {id(d_copy)}")
"""
Memory address of first dictionary => 4378770304
Memory address of second dictionary => 4387913280
"""
"""
10. Nested Dictionary
"""
s1 = {"name": "Alice", "age": 19}
s2 = {"name": "Bob", "age": 20}
s3 = {"name": "John", "age": 21}
students = {"student_one": s1, "student_two": s2, "student_three": s3}
print(students)

print(students["student_one"]["name"])
# Access the elements in nested list
new_dict: Dict[str, str] = {}
# print(f"Student one name =>{students["student_one"]["name"]}")
# Student one name =>Alice

# Loop through nested dictionary
for k, v in students.items():
    print(f"Complete object: {k}=> {v}")
    for i in v:
        print(f"Detail about each object: {i}=> {v[i]}")
"""
Complete object: student_one=> {'name': 'Alice', 'age': 19}
Detail about each object: name=> Alice
Detail about each object: age=> 19
Complete object: student_two=> {'name': 'Bob', 'age': 20}
Detail about each object: name=> Bob
Detail about each object: age=> 20
Complete object: student_three=> {'name': 'John', 'age': 21}
Detail about each object: name=> John
Detail about each object: age=> 21
"""

# Insert elements in dictionary using for loop
# new_dict = {}
# size_dict = int(input("Enter the size of the dictionary: "))
#
# for i in range(size_dict):
#     key = input("Enter the key: ")
#     value = input("Enter the value: ")
#     new_dict[key] = value
# print(f"Dictionary after insertion: {new_dict}")
