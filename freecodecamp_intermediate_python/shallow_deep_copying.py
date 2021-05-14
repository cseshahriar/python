# copying
import copy

my_list = [1, 2, 3, 4, 5]

cpy_list = copy.copy(my_list)

# cpy_list = my_list.copy()
# cpy_list = list(my_list) # shallow copy
# cpy_list = my_list[:]

cpy_list[0] = -10 # original change

print(my_list) # [[-10, 2], [3, 4]]
print(cpy_list) # [-10, 2, 3, 4, 5]


# shallow vs deep
# - shallow copy: one level deep, only references of nested child object
# - deep copy: full independent copy
print('deep copy')
nested_list = [[1,2],[3,4]]
cpy2 = copy.deepcopy(nested_list) # actual copy
cpy2[0][0] = -10
print(cpy2) # [[-10, 2], [3, 4]]
print(nested_list) # [[-10, 2], [3, 4]]

# class 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Shahriar', 28)
p2 = copy.copy(p1) # shallow copy

p2.age = 30

print(p1.age) # 28
print(p2.age) # 30