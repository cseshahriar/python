# python numbers 
"""
There are three numeric types in Python:
int
float
complex
"""

# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 1 # int 

# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
# Float can also be scientific numbers with an "e" to indicate the power of 10.
y = 2.8 # float
ye = 35e3

# Complex numbers are written with a "j" as the imaginary part:
z = 1j   # complex
ze = 2 + 3j

print(x, type(x))
print(x, type(y))
print(x, type(ye))
print(x, type(z))
print(x, type(ze))

# Type Conversion
cx = float(x)

# Random Number
import random
random_num = random.randrange(1,10)
print(random_num)

# Python Casting
x = int(1) # int() - constructs 
y = int(2.8)
z = int("3") # z will be 3
m = str(3.0) // '3.0'