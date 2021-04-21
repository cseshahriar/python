# Tuple: ordered, immutable, allows duplicate elements
my_tuple = (1,2,3,4,5,6)
print(my_tuple)

my_tuple2 = "max", 28, "boston"
print(my_tuple2)
print(type(my_tuple2))

my_tuple3 = tuple([1,2,3,4, 5])
print((my_tuple3))

item = my_tuple[0]
print(item)

# my_tuple[0] = 'Tim' # not posible

# loop
for i in my_tuple:
    print(i)

# checking
if 1 in my_tuple:
    print('True')
else:
    print('False')

# length
my_tuple = ('a', 'e', 'i', 'o', 'u')
print(len(my_tuple))

# count
print(my_tuple.count('o'))

# index 
print(my_tuple.index('o'))

# tuple to list
my_list = list(my_tuple)
print(my_list)

# list to tuple 
my_tuple = tuple(my_list)
print(my_tuple)

# slicing 
my_tuple = (1,2,3,4,5,6,7,8,9)
b = my_tuple[2:5] # start, stop
print(b)

c = my_tuple[::1] # step like loop
print(c)

d = my_tuple[::2]
print(d)

e = my_tuple[::-1] # reverse
print(e)

# unpacking 
my_tuple = "max", 28, "boston"
name, age, city = my_tuple
print(name, age, city)

my_tuple = (1,2,3,4,5)
i1, *i2, i3 = my_tuple
print(i1, i2, i3)

# tuple are more effeicient when we working with large data

# memory diff
import sys
my_list = [0, 1, 2, 'hellow', True]
my_tuple = (0, 1, 2, 'hellow', True)
print(sys.getsizeof(my_list, 'bytes')) # 96
print(sys.getsizeof(my_tuple, 'bytes')) # 80

# time diff
import timeit
print(timeit.timeit(stmt="[1,2,3,4,5]", number=1000000)) # 1 milons time to create a list
print(timeit.timeit(stmt="(1,2,3,4,5)", number=1000000))