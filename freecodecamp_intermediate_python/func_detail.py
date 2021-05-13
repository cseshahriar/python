"""
Function arguments in details:
- The difference between arguments and parameters
- Positional and keyword arguments
- Default arguments
- Variable-length arguments(*args, **kwargs)
- Container unpacking into function arguments
- Local vs, global arguments
- Parameter passing(by value or by reference)
"""

# The difference between arguments and parameters
def print_name(name): # name is parameter
    print(name)

print_name('Shahriar') # this is argument

# Positional and keyword arguments
def foo(a, b, c):
    print(a, b, c)

foo(1, 2, 3) # Positional
foo(c=1, a=2, b=3) # keyword arguments

# Default arguments
def print_age(age=28): # 28 is default age
    print(age)

print_age()

# Variable-length arguments(*args, **kwargs)
def my_foo(a, b, *args, **kwargs): 
    # *args means pass any number of args
    # **kwargs means pass any number of kwargs
    print(a, b)
    
    for arg in args:
        print(arg)

    for key in kwargs:
        print(key, kwargs[key])

my_foo(1,2, 3,4,5, six=6, seven=7)

# Container unpacking into function arguments
def my_another_foo(a,b,c):
    print(a,b,c)

# my_list = [0,1,2]
# my_list = (0,1,2)
my_list = {'a':1, 'b':2, 'c':3}
my_another_foo(**my_list) # if *dict returns keys ** dict returns value

# Local vs, global arguments
def foo2():
    # if modify golbal
    # global number # access blobal number var
    # number = 3
    x = number # x is local
    print('number inside function ', x)


number = 0 # global
foo2()

# Parameter passing(by value or by reference)
# call by object or object references

def final_foo(x): 
    x = 5 # like default 

var = 10 
final_foo(var)
print(var) # 10