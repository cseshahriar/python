# Itertools: product, permutations, combinations, accumulate, grouplate, groupby, and infinite iterators
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby
import operator
# product
a = [1,2]
b = [3,4]
my_product = product(a,b)
print(list(my_product)) # [(1, 3), (1, 4), (2, 3), (2, 4)]

# permutations
a = [1,2,3]
perm = permutations(a, 2)
print(list(perm))
"""
all possible combination
[
    (1, 2, 3), 
    (1, 3, 2), 
    (2, 1, 3), 
    (2, 3, 1),
    (3, 1, 2), 
    (3, 2, 1)
]
if pass 2
[
    (1, 2),
    (1, 3),
    (2, 1),
    (2, 3),
    (3, 1),
    (3, 2)
]
"""

# combinations
print('combinations')
c = [1,2,3,4]
comb = combinations(c, 2)
print(list(comb))
"""
[
    all possible combinations with length 2
    (1, 2), 
    (1, 3), 
    (1, 4), 
    (2, 3), 
    (2, 4), 
    (3, 4)
]
"""

# combinations_with_replacement
comb_with = combinations_with_replacement(c, 2)
print(list(comb_with))
""" 
[
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (2, 2),
    (2, 3),
    (2, 4),
    (3, 3),
    (3, 4),
    (4, 4)
    ]
"""

# accumulate
# accumulate_var = accumulate(c)
accumulate_var = accumulate(c, func=operator.mul) # func=max
print(c)
print(list(accumulate_var))
"""
[1, 2, 3, 4]
[1, 3, 6, 10] # 1+2 = 3, 3+3 = 6, 6 + 4 =10
[1, 2, 6, 24] # 1*2 = 2 , 2*3 = 6, 6 * 4 = 24
"""

# groupby
def smaller_than(x):
    return x < 3

g = [1,2,3,4]
gr = groupby(g, key=smaller_than)
for key, val in gr:
    print(key,list(val))