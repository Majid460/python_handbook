"""
In this file we will see different operations on numbers.
How to use numbers in python

Python operates on different datatypes of numbers.
1. Integers  ->  int (Integer (whole number)	x = 10)
2. Float ->  float  (Floating point (decimal)	pi = 3.14)
3. Complex ->  complex  ( Complex numbers	z = 2 + 3j )
"""

"""
Operations on numbers

Addition = +  -> 2+2
Subtraction =  -  -> 2-2
Multiplication = *  -> 2*2
Division = /  -> 2 / 2
Floor Division = //  -> 2 // 2  (	Integer division (drops decimal))
Power = ** -> 2**2  equals to 2^2
Modulus = %  -> 2%2   (Remainder of division) like 0 in this case
"""

"""
Precedence of operators
1. Parentheses () (2*2)
2. Exponential 2**2 -> 2^2
3. Unary plus and minus ->  +2, -2
4. Multiplication, Division  -> *, /, //, %
5. Addition and Subtraction ->  +, -
6. Assignment Operator -> =
"""
# Basic Arithmetic
print(f"Addition = {2+2}")
# prints 4

print(f"Precedence of 50 - 5 * 6 = {50 - 5 * 6}")  # First multiply and then subtract
# prints 20

print(f"Precedence test of (50 - 5 * 6) / 4  = {(50 - 5 * 6) / 4}")  # first parentheses and then divide
# print 5.0

print(f"Division of 8/5 = {8/5}")  # division always returns the floating number
# prints 1.6

# Complex Arithmetic

# Floor (To convert the floating of division into integer)
print(f"Floor of 17//5 = {17//5}")
# prints 3

# Modulus operator % (Returns the remainder)
print(f"Mod of 5%3 = {5%3}")
# prints 2

# Power **
print(f"Power 5^3 = {5**3}")
# prints 125

# Example of Numbers
# Example 1
"""
Armstrong Number checker (it is a number that is equal to the sum of its 
digits each raised to the power of the number of digits.)
Example = 153 → 1³ + 5³ + 3³ = 153

1. Input number
2. Convert to string
3. Calculate the length
4. Split the string
5. Apply loop and 
   5.1. loop to the each character of string 
   5.2. Convert the each character to int and apply power of length
   5.3. Add in the output number
"""
# Solution 1 (Simple)
num = int (input("Enter a number: "))
str_of_num = str(num)
len_of_num = len(str_of_num)
output_num = 0


for i in str_of_num:
    output_num += int(i)**len_of_num
if output_num == num:
    print("The number {0} is an Armstrong ".format(num))
else:
    print("The number {0} is Not an Armstrong ".format(num))

# Solution 2 (List comprehensions)

num = int (input("Enter a number: "))
str_of_num = str(num)
len_of_num = len(str_of_num)
sum_of_num = sum(int(i)**len_of_num for i in str_of_num)
if sum_of_num == num:
    print("The number {0} is an Armstrong ".format(num))
else:
    print("The number {0} is Not an Armstrong ".format(num))


# Example 2
"""
Reverse a number
Write a Python program to reverse the digits of a given integer.

E.g. Enter a number: 12345
Output: Reversed number is: 54321
"""
num = int (input("Enter a number: "))
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num*10+digit
    num = num//10
print(f"Reversed number of {num} is {reversed_num}")
