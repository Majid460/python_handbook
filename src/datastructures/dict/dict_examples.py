"""
Practice tasks for dictionaries in python
"""

"""
1. Create two dictionaries and then merge them.
"""
from typing import Counter


a = {"a": 1, "b": 2}
b = {"c": 3, "d": 4}

# merged = a|b
# Merged dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# OR
# merged = {**a,**b}
# Merged dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(f"Merged dictionary: {a}")

"""
2. Write a program to count word frequency in a sentence using a dictionary.
Example: "this is a test this is" → {'this': 2, 'is': 2, 'a': 1, 'test': 1}
"""
test_str = "this is a test this is"
cnt = Counter(test_str)
print(cnt)
count_words = {}
for word in test_str.split():
    count_words[word] = count_words.get(word, 0) + 1

print(f"Counting words:=> {count_words}")
# Counting words:=> {'this': 2, 'is': 2, 'a': 1, 'test': 1}

"""
3. Store countries and their capitals in a dictionary. Ask the user for a country and print its capital.
"""
# country_and_cap = {"Ireland": "Dublin", "Pakistan": "Islamabad", "India": "Delhi", "Uk": "London",
#                    "USA": "Washington DC", "Germany": "Berlin", "Canada":"Ottawa"}
# print("Countries::",end='\n')
# var = {print(x) for x in country_and_cap.keys()}
# country = input("From all the given countries enter a name of country and check the capital:")
# for k,v in country_and_cap.items():
#     if k.lower()==country.lower():
#         print(f"The capital of {country} is {v}")
#         break

"""
3. Print the name of the student with the highest marks
"""
s1 = {"name": "Alice", "age": 19, "marks": 90}
s2 = {"name": "Bob", "age": 20, "marks": 89}
s3 = {"name": "John", "age": 21, "marks": 100}
students = {"student_one": s1, "student_two": s2, "student_three": s3}
# Find Max mark student
highest_marks_std = {}
max_value = int(-1)
for k, v in students.items():
    # At this level we are on per object of students
    if v.get("marks") > max_value:
        max_value = v.get("marks")
        highest_marks_std = v

print(f"highest => {highest_marks_std} ")
# highest= > {'name': 'John', 'age': 21, 'marks': 100}

# Find Min mark student
min_marks_std = {}
min_value = int(-1)
for k, v in students.items():
    if v.get("marks") < max_value:
        max_value = v.get("marks")
        min_value = v

print(f"Minimum mark student => {min_value} ")
# Minimum mark student => {'name': 'Bob', 'age': 20, 'marks': 89}

"""
Short method to find min and max
"""
"""
x[0] (student_id): student_one
x[1] (student_info): {'name': 'Alice', 'age': 19, 'marks': 90}
x[1]['marks']: 90
"""
highest_marks_std = max(students.items(), key=lambda student: student[1]["marks"])
print(f"highest using lambda => {highest_marks_std} ")


# highest using lambda => ('student_three', {'name': 'John', 'age': 21, 'marks': 100})
# Using simple function
def tuple_break(student_tuple):
    return student_tuple[1]["marks"]


highest_marks_std = max(students.items(), key=tuple_break)
print(f"highest using simple function => {highest_marks_std} ")
# highest using simple function => ('student_three', {'name': 'John', 'age': 21, 'marks': 100})

"""
Write a program to invert a dictionary (swap keys and values).
Example: {"a": 1, "b": 2} → {1: "a", 2: "b"}
"""
original = {"a": 1, "b": 2, "c": 3}
reverted = {}
for k, v in original.items():
    reverted[v] = k
print(f"Reverted dict => {reverted}")
# Reverted dict => {1: 'a', 2: 'b', 3: 'c'}

# Using comprehension
rev = {v: k for k, v in original.items()}
print(f"Reverted dict => {rev}")
# Reverted dict => {1: 'a', 2: 'b', 3: 'c'}
