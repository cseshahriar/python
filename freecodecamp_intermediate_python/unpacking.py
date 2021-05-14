# ***************************** asterisk
# multiplying
result = 5 * 7
print(result) # 35

# sqrt
result = 2 ** 4
print(result) # 16

# list tricks
zeros = [0,1] * 10
print(zeros)  # [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

# function
def foo(a, b, c, *args, **kwargs):
    print(f'a : {a} b: {b}')
    
    print('args:')
    for arg in args:
        print(arg)

    print('kwargs:')
    for key in kwargs:
        print(key, kwargs[key])

foo(1,2,3,4,5, six=6, seven=7)

def foo2(a, b, c):
    print(a, b, c)

my_dict = {'a':1, 'b':2, 'c': 3}
foo2(**my_dict) # unpacking

# unpacking
numbers = [1,2,3,4,5,6]
# numbers = (1,2,3,4,5,6)
*begaining, last = numbers
print('begaining ', begaining) # [1, 2, 3, 4, 5]
print('last ', last) # 6


my_tuple = (1,2,3)
my_list = [4,5,6]
my_set = {7, 8, 9}
new_list = [*my_tuple, *my_list, *my_set]
print(new_list)

dict_a = {'a':1, 'b':2, 'c': 3}
dict_b = {'c': 3, 'd':4}
my_dict = {**dict_a, **dict_b} # argument unpacking
print(my_dict)