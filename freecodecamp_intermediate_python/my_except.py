# Errors and Exceptions: syntex error and exception

# syntex error 
a = 5 
# print(a)) # error

# exceptions
# a = 5 + '10' # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# builtin exceptions
# import somemodule # ModuleNotFoundError: No module named 'somemodule'
# b = c # NameError: name 'c' is not defined

# file error
# f = open('somefile.txt')

# value error 
a = [1,2,3]
# a.remove(4) # ValueError: list.remove(x): x not in list
# print(a)

# a[4] # IndexError: list index out of range

my_dict = {'name': 'max'}
# my_dict['age'] # key error

# raising exceptions
x = -5 # -5 for exception
# if x < 0:
#     raise Exception('x should be positive')
# print(x)

# assert(x>0) , 'x is not positive'


# handle exception
try:
    a = 5 / 1
    b = 5 + 'b'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('ok')    
finally:
    print('cleaning up')
# try:
#     b = 6 / 0
# except Exception as e:
#     print(e)

# try:
#     c = 7 / 0
# except ZeroDivisionError:
#     print('can\'t divide by zero')

# create exception class
class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    """ text value method """
    if x > 100:
        raise ValueTooHighError('Value is too high')
    if x < 5:
        raise ValueTooSmallError('value is too small', x)    

try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)