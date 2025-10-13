"""
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
"""
print("\n----------- Functions -------------\n")


# To Create a function python use a def keyword

def test():
    print("A generic function")


# This function runs when it is called so
test()
# prints -> A generic function

print("\n----------- Arguments passing -------------\n")
"""
There are many ways to pass parameters in the function such as
- Positional Parameters
- Arbitrary Arguments, *args
- Keyword Arguments
- Arbitrary Keyword Arguments, **kwargs
- Positional Only Arguments
- Keyword Only Arguments
"""


# By default, a function must call with correct number of parameters
def user(firstname, lastname):
    print(f"{firstname} {lastname}")


# Call this function
user("Test", "one")


# Prints -> Test one

# If we don't know the number of arguments to pass then we name them arbitrary arguments *args
# Represented by *arg


def user(*args):  # User will get tuple
    firstname = args[0]  # get the values from tuple based on the index
    lastname = args[1]
    age = args[2]
    print(f"User detail => {firstname} {lastname} {age}")


# I initialize a tuple
user_data = ("Test", "Two", 20)
user(*user_data)  # Before passing it to function I unpack it to separate the values
# User detail => Test Two 20

"""
Keyword Arguments
- You can also send arguments with the key = value syntax.
- This way the order of the arguments does not matter.

These are represented by **kwargs
"""


# user will receive a dictionary and then get the values from the dictionary based on the key values
def user(**kwargs):
    first_name = kwargs["firstname"]
    last_name = kwargs["lastname"]
    age = kwargs["age"]
    print(f"Users details by **kwargs => {first_name} {last_name} {age}")


dictionary = {"firstname": "Test", "lastname": "two", "age": 20}
user(**dictionary)


# Users details by **kwargs => Test two 20

# To pass a default parameter value
def user(firstname="None"):
    print(f"Default value of firstname => {firstname}")


user()


# Default value of firstname => None

# Passing List as arguments
def user(addresses):
    [print(f"Addresses of user {address}") for address in addresses]


addr = ["first", "second", "third"]
user(addr)
"""
Addresses of user first
Addresses of user second
Addresses of user third
"""


# Return values from function

def calculate_area(length, width):
    return length * width


area = calculate_area(10, 20)
print(f"Area is with return base test :: {area}")
# Area is :: 200

"""
The pass Statement
Function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
"""
def myfunction():
  pass
myfunction()

"""
Positional-Only Arguments

- You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
- To specify that a function can have only positional arguments, add , / after the arguments:
"""
def cal_area(length,width,/):
    return length*width

#area = cal_area(length = 10,width = 20)
#print(f"Area is :: {area}")

# We will get error because we have to pass positional arguments just not any keyword argument
"""
area = cal_area(length = 10,width = 20)
Error:
Traceback (most recent call last):
  File "/Users/macbookpro/Documents/Python Practice/python_practice_part1/core/basic/functions/functions.py", line 132, in <module>
    area = cal_area(length = 10,width = 20)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: cal_area() got some positional-only arguments passed as keyword arguments: 'width'
"""

# To fix it we need to pass only positional because we have used forward slash (/) right after the end of arguments
area = cal_area(10, 20)
print(f"Area is with Positional-Only Arguments (/) end of args:: :: {area}")

# Area is :: 200

"""
Keyword-Only Arguments

- To specify that a function can have only keyword arguments, add *, before the arguments:
"""
def calc_area(*,length,width):
    return length*width

area = calc_area(length = 10, width =  20)
print(f"Area with is Keyword-Only Arguments (*) before args:: {area}")
# Area with is Keyword-Only Arguments (*) before args:: 200

"""
Combine Positional-Only and Keyword-Only
You can combine the two argument types in the same function.

Any argument before the / , are positional-only, and any argument after the *, are keyword-only.

Example

"""
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)