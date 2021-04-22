# Sets: unordered, mutable, on duplicates
myset = {1, 2, 3, 4, 5, 6, 6}
print(myset)

myset = set([1,2,3,4,5])
print(myset)

myset = set('hellow')
print(myset) # {'o', 'l', 'w', 'h', 'e'} 

myset = {}
print(type(myset)) # dict

# add 
myset = set()
myset.add(1)
myset.add(3)
myset.add(4)
myset.add(4)
print(myset)

# remove 
myset.remove(4)
print(myset)

myset.discard(4) # if not exist it's ok, no error

print(myset.pop()) # last el

# set clear
myset.clear()

# loop
myset = {1,2,3,4,5,6}
for i in myset:
    print(i)

# check
if 1 in myset:
    print('True')
else:
    print('False')

# union
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

u = odds.union(evens) # return new set
print(u)

i = odds.intersection(primes) # return new set
print(i)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
diff = setB.difference(setA) # return new set
print(diff)

deff = setB.symmetric_difference(setA) # return new set
print(diff)

setA.update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.intersection_update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3}
subset = setA.issubset(setB)
print(subset)

superset = setA.issuperset(setB)
print(superset)

dis = setA.isdisjoint(setB)
print(dis)

# copy 
setA = setB.copy() # set()

# frozenset
a = frozenset([1,2,3,4,5,6]) # can't change/update
print(a)