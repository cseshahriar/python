# Random Numbers:
import random

# psudo random number
a = random.random()
print(a) # range 0,1 float

b = random.uniform(1,5) # float
print(b)

c = random.randint(1, 10)
print(c)

d = random.randrange(1,10) # skip upper bound
print(d)

e = random.normalvariate(0, 1) # it's for stastics
print(e)

# random for Sequence

mylist = list('AAGCDDEFGH')
# random choice
random_choice = random.choice(mylist) # pic random element
print(random_choice)

# random unique has many choice
random_sample = random.sample(mylist, 3)
print(random_sample) 

# random choices(can be duplicate)
random_choices = random.choices(mylist, k=3)
print(random_choices)

# random shuffle
mylist = list('AABBCDEFFGH') 
random.shuffle(mylist)
print(mylist)

# seed / no change
"""
The seed() method is used to initialize the random number generator.
The random number generator needs a number to start with (a seed value), to be able to generate a random number.
If you use the same seed value twice you will get the same random number twice. 
"""
random.seed(1)
print(random.random()) # always same
print(random.randint(1, 10)) # always

random.seed(2)
print(random.random()) # always same
print(random.randint(1, 10)) # always

import secrets
a = secrets.randbelow(10)
print(a)
# 8 4 2 1
# 1 1 1 1 = 15 
a = secrets.randbits(4) # random bits
print(a)

mylist = list('AABBCDEFFGH')
a = secrets.choice(mylist)
print(a) 

# numpy random
import numpy as np

a = np.random.rand(3)
# a = np.random.rand(3,3)
a = np.random.randint(0,10,(2,3)) # 2/3 arr
print(a)
arr = np.arr([1,2,3,4,5], [3,4,3])
np.shuffle(arr)
print(arr)
