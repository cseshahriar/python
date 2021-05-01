# lambd arguments: expression
add10 = lambda x: x + 10 # x argument
print(add10(5))

mull = lambda x,y: x * y
print(mull(3,4))

# sorted 
pointers2D = [(1,2), (15, 1), (5, -1), (10, 4)]
pointers2D_sorted = sorted(pointers2D, key=lambda x: x[1]) # sort by second value
print(pointers2D_sorted)
pointers2D_sorted = sorted(pointers2D, key=lambda x: x[0] + x[1]) # sort by second value
print(pointers2D_sorted)

# map(func, seq) : The function to execute for each item
a = [1,2,3,4,5]
b = list(map(lambda x: x * 2, a)) # each el multiply by 2
print(b)

# same with list comprenshion
c = [x*2 for x in a]
print(c)

# filter(fubc, seq): A Function to be run for each item in the iterable
f = [1,2,3,4,5,6]
filter_data = list(filter(lambda x: x % 2 == 0, f)) # return true, false
print(filter_data)

# same with list comprenshion
list_data = [x for x in f if x % 2 == 0]
print(list_data)

# reduce func: apply a particular function passed in its argument to all of the list elements
# return a single value
import functools
r = [1, 2, 3, 4] # 24
prod_a = functools.reduce(lambda x,y: x * y , r) # two arg req
print(prod_a)