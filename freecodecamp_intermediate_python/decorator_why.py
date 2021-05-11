# decorator act as a wrapper for your original func
# common use casees of decorators are 1. loggin 2. timing
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