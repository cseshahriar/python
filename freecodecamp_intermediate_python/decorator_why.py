""" 
A decorator is a design pattern in Python that allows a user to 
add new functionality to an 
existing object without modifying its structure.
Decorators are usually called before the definition of a function you want to decorate.
"""
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__+" took " + str( (end-start)*1000) + " mil sec")
        return result

    return wrapper

@time_it
def cal_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

array = range(1, 100000)
cal_square(array)
calc_cube(array)



def uppercase_decorator(function):
    """ make uppercase """
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    
    return wrapper

def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.splite()
        return splitted_string

    return wrapper

@split_string
@uppercase_decorator
def say_hi():
    print('Hello World')

say_hi()


def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1,arg2))
        function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))

cities("Nairobi", "Accra")