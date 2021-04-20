# List: ordered, mutable, allows duplicate element, collection data type
my_list = ['banana', 'cherry', 'apple']
print(my_list)

my_list2 = [4, True, 'apple', 'apple'] 
print(my_list2)

# access
item = my_list[-3] # 0, 1, 2, -1, -2, -3
print(item)

# loop
for i in my_list:
    print(i)

# check item is exist
if 'banana' in my_list:
    print('yes')
else:
    print('no')

# length 
list_length = len(my_list)
print(list_length)

# append item
my_list.append(3)
print(my_list)

# insert by index
my_list.insert(1, 'blueberry')
print(my_list)

# remove item 
item = my_list.pop() # remove last item
print(item)
print(my_list)

item = my_list.remove('blueberry') # remove item
print(item)
print(my_list)

# reverse 
my_list.reverse()
print(my_list)

# short
print(my_list) # ['apple', 'cherry', 'banana']
print(my_list) # ['apple', 'cherry', 'banana']

my_list = [4, 3, 1,-1, -5, 10]
my_list.sort()
print(my_list) 

# new_list from sorted
new_list = sorted(my_list)
print(new_list)

# tricks
my_list = [0] * 5
print(my_list)

# concate 
my_list3 = my_list + my_list2
print(my_list3)

# slicing 
my_list = [1,2,3,4,5,6,7,8,9]
a = my_list[1:5] # start: stop(upper limit exclude, or stop index)
print(a) # [2, 3, 4, 5]

b = my_list[:5] # from begaining
print(b) # [1, 2, 3, 4, 5] (upper limit is exclude or stop index)

c = my_list[5:]
print(c)


# step index (like loop)
a = my_list[::1] # step 1  
print(a) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = my_list[::2] 
print(a) # step 2 [1, 3, 5, 7, 9]

b = my_list[::-1] # decrement step, it's reade from last
print(b)

# copy lsit 
list_original = ['banana', 'cherry', 'apple']

list_copy = list_original # its not copy, it's assign
print(list_copy)

# bad practice
# list_copy.append('jackfruid')
# print(list_copy)
# print(list_original) # also modify original list

# list copy 
list_copy = list_original.copy() # or list(list_origin), or [:] for copy
list_copy.append(1)
print(list_copy)
print(list_original) # not change


# sqrt 
my_list = [1,2,3, 4, 5]
my_sqrt = [i*i for i in my_list]
print(my_sqrt)

# remove all
my_list.clear()
print(my_list)