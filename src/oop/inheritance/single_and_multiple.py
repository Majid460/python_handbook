"""
-------------------Inheritance -----------------
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class. (Base Class)

Child class is the class that inherits from another class, also called derived class. (Derived Class)

Key Points:
Inheritance in Python classes

- A derived class is defined using the syntax:
class DerivedClassName(BaseClassName):
    <statements>


- The BaseClassName must be accessible in the current scope, but arbitrary expressions (e.g., modname.BaseClassName) are also allowed.
- Execution and attribute resolution
- When a derived class is created, the base class is stored internally.

- Attribute lookup follows the inheritance chain: if not found in the derived class, Python searches in the base class (recursively if multiple levels of inheritance).

- Instantiation

- Instantiating a derived class works the same as a base class:
- obj = DerivedClassName()

- Method resolution
- Methods are looked up through the inheritance chain.
- Derived classes can override methods from their base class.
- All methods in Python act like virtual methods (C++ comparison): overridden methods in the derived class are automatically used.

- Extending base class methods

- A derived class method can extend (not just replace) a base class method by explicitly calling it:
- BaseClassName.methodname(self, args)

- Built-in functions for inheritance
- isinstance(obj, Class) → checks if obj is an instance of Class or its subclasses.
- issubclass(Derived, Base) → checks if Derived is a subclass of Base.

"""
from dataclasses import dataclass


# Base Class
class Person:
    def __init__(self,*, firstname, lastname,): # Remember * represents it has keyword based arguments
        self.firstname = firstname
        self.lastname = lastname
    def print_name(self):
        print(f"Person name is {self.firstname} {self.lastname}")

p = Person(firstname="Test",lastname="user")
p.print_name()
# Person name is Test user

## Derived Class
class Student(Person):
    """
    Now we have successfully added the __init__() function, and kept the inheritance of the parent class,
    and we are ready to add functionality in the __init__() function.
    """
    def __init__(self, firstname, lastname,year):
        super().__init__(firstname=firstname, lastname=lastname)
        self.graduation_year = year

    """
    By using the super() function, you do not have to use the name of the parent element,
     it will automatically inherit the methods and properties from its parent.
    """
    def print_name(self):
        return print(f"Student name is {self.firstname} {self.lastname} year {self.graduation_year}")

    #Without inheritance of init function from parent

    # def __init__(self, firstname, lastname):
    #     self.firstname = firstname
    #     self.lastname = lastname

s1 = Student("Student", "1",2019)
s1.print_name()
# Student name is Student 1 year 2019


# Multiple Inheritance
"""
- Multiple inheritance syntax

- A class can inherit from multiple base classes:
- class DerivedClassName(Base1, Base2, Base3):
    <statements>

- Attribute lookup order (simplified view)
- Search is left-to-right across the base classes.
- Proceeds depth-first into each base class hierarchy.
- A class is not searched twice if already visited.

- Method Resolution Order (MRO)

- Python uses a dynamic algorithm (C3 linearization) to determine search order.
- Ensures cooperative use of super(), enabling each class in the hierarchy to contribute.
- Known as call-next-method in some languages.

- Diamond problem handling
- Multiple inheritance often creates “diamond” relationships (same ancestor reached through multiple paths).
- Example: all classes ultimately inherit from object, leading to multiple paths to it.

- Linearization rules (Python’s solution)

- Left-to-right precedence (follows class definition order).
- Each class called once (avoids duplicate visits).
- Monotonicity: subclassing does not alter parent precedence order.
- Guarantees reliability and extensibility when designing classes.

- Practical impact
- Developers can safely use multiple inheritance without worrying about ambiguous lookups.

- super() works consistently across complex hierarchies.
 In short: Python’s multiple inheritance is powerful, thanks to MRO ensuring predictable, cooperative method calls.
"""
class Shape:
    def display(self):
        return print("Class shape ")
    
class Circle(Shape):
    def display(self):
        print("Circle class")

class Square(Shape):
    def display(self):
        print("Square class")

class Cylinder(Square,Circle): # As it looks (LTR) so it will print square class
    pass

cy = Cylinder()
cy.display()
# Square class
# It never prints the circle class because:
#This happens because Python looks at the MRO (Cylinder → Square → Circle → Shape → object) and finds display() in Square first.

# To solve this problem use super like in the following example

"""
The given code does not give Diamond Problem in python because the python resolves multiple inheritance dispute using the Method Resolution order in short we can call it MRO .
"""
"""
        shape
          ^
          |
   -----------------
   |               |
 circle         square
   ^               ^
    \             /
     \           /
      \         /
       \       /
        \     /
        cylinder

MRO (Method Resolution Order):
cylinder → circle → square → shape → object

"""
# Another example of diamond problem with MRO
class Shape:
    def greet(self):
        print("class shape called")
class Circle(Shape):
    def greet(self):
        super().greet()
        print("Class is Circle")
class Square(Shape):
    def greet(self):
        super().greet()
        print("Class is Square")

class Cylinder(Circle,Square):
    def greet(self):
        super().greet()
        print("Class is Cylinder")

cyl = Cylinder()
cyl.greet()
"""
class shape called
Class is Square
Class is Circle
Class is Cylinder
"""


"""
Forward Chain:
1. cyl called Cylinder.greet(), it called to super.greet() which is Circle
2. Circle called again super.greet() and printed the shape
-- MRO -- Next MRO is square in Cylinder
3. It after printing the square it goes to square and prints out
-- Reverse chain
4. Then after printing the square it called the circle print
5. Then final cylinder 

Calling Flow
cylinder.greet()
   ↓
circle.greet()
   ↓
square.greet()
   ↓
shape.greet()
   ↑
square prints "class square called"
   ↑
circle prints "class circle called"
   ↑
cylinder prints "class cylinder called"
"""
# Private Variables
"""
Private Variables in Python

In Python, private variables are declared by prefixing with double underscores __.

Example:

class Parent:
    def __init__(self):
        self.__secret = "This is private"


These variables are name-mangled by Python → internally stored as _ClassName__varname.

So self.__secret in Parent is stored as self._Parent__secret
"""


class Parent:
    def __init__(self):
        self.__secret = "parent secret"

    def show_secret(self):
        print(self.__secret)


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__child_secret = "child secret"

    def show_child_secret(self):
        print(self.__child_secret)

    # Trying to override parent private variable
    def try_access_parent_secret(self):
        # This will raise AttributeError if you try self.__secret
        # print(self.__secret) ❌

        # Correct way (via name mangling)
        print(self._Parent__secret)


c = Child()
c.show_secret()  # Parent method → "parent secret"
c.show_child_secret()  # Child method → "child secret"
c.try_access_parent_secret()  # Access via mangled name → "parent secret"

"""
Private (__var) in Parent is not visible as-is in Child.
Child can still access it via _Parent__var (name mangling).
Best practice:
Use single underscore _var for “protected” variables → signals “internal use” but still accessible to subclasses.
Use getter/setter methods or @property for controlled access instead of exposing __var.
"""

# Set and get

class BankAccount:
    def __init__(self,balance):
        # private variable
        self.__balance = balance

    # Getter
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,amount):
        if amount<0:
            print("Balance cannot be negative")
        else:
            self.__balance = amount

    @balance.deleter
    def balance(self):
        print("Deleting balance...")
        del self.__balance


account = BankAccount(100)
#account.balance = -1
# Balance cannot be negative

account.balance = 200
print(account.balance)
# 200
del account.balance
# Deleting balance...


# Data class:
"""
What is a Data Class?

Introduced in Python 3.7 via the dataclasses module.

A @dataclass automatically generates:

__init__() → constructor

__repr__() → string representation

__eq__() → comparison

Optionally __hash__()

Makes it easier to create classes meant for storing data only (like DTOs in other languages).
"""

@dataclass
class User:
    name:str
    age:int
    __email:str = None

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,email):
        self.__email = email

    @email.deleter
    def email(self):
        print("email deleted...")
        del self.__email

user = User("Test",10)
user.email = "a@gmail.com"
print(f"Email is:: {user.email}")
del user.email
print(user)
"""
Email is:: a@gmail.com
email deleted...
"""
# User(name='Test', age=10)

# Data class with Methods

@dataclass
class Rectangle:
    width: int
    height: int

    def area(self) -> int:
        return self.width * self.height

r = Rectangle(5, 10)
print(r)          # Rectangle(width=5, height=10)
print(r.area())   # 50

"""
Rectangle(width=5, height=10)
50
"""