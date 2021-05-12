# Generators: generator are a function that return a object
# its effecient with large data set.

def my_generator():
    yield 1
    yield 2
    yield 5
    yield 4

g = my_generator()
# print(g) # return generator object

# # looging
# for item in g:
#     print(item) 

# # output with next func
# value = next(g)
# print(value)

# value = next(g)
# print(value)
print(sorted(g)) # sorte list

# example 
def countdown(num):
    print("starting")
    while num > 0:
        yield num
        num -= 1

cd = countdown(4) # generator obj

value = next(cd)
print(value)

value = next(cd)
print(value)

# generator are very memory effecient
import sys

def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(sys.getsizeof(firstn(10000000))) # 81528048
print(sys.getsizeof(firstn_generator(10000000))) # 112

# example 
def fibonacci(limit):
    # 0 1 2 3 5 8 13 21
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)

for i in fib:
    print(i)

# generator expression
my_generator = (i for i in range(10) if i % 2 == 0)
print(sys.getsizeof(my_generator)) # 112

mylist = [i for i in range(10) if i % 2 == 0]
print(sys.getsizeof(mylist)) # 120

