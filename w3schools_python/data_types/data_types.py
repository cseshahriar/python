# Built-in Data Types
""" 
Text Type     :	str
Numeric Types :	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type  :	dict
Set Types     :	set, frozenset
Boolean Type  :	bool
Binary Types  :	bytes, bytearray, memoryview
"""

x = "Hello World"  # str

"""
The int data type deals with integers values.
 This means values like 0, 1, -2 and -15, and not numbers like 0.5, 1.01, -10.8, etc. 
"""
x = 20  # int

"""The float data type can represent floating point numbers, up to 15 decimal places. 
This means that it can cover numbers such as 0.3, -2.8, 5.542315467, etc. but also integers.
"""
x = 20.5  # float

"""
The last numeric type we need to cover is the complex type. 
It's a rarely used data type, and its job is to represent imaginary numbers in a complex pair.

The character j is used to express the imaginary part of the number,
unlike the i more commonly used in math.
"""

x = 1j  # complex
x = ["apple", "banana", "cherry"]  # list
x = ("apple", "banana", "cherry")  # tuple
x = range(6)  # range
x = {"name": "John", "age": 36}  # dict
x = {"apple", "banana", "cherry"}  # Set
x = frozenset({"apple", "banana", "cherry"})  # frozenset
x = True  # bool
x = b"Hello"  # bytearray
x = memoryview(bytes(5))  # memoryview


# Type Conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
