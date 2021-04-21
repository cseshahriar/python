# Dictionary: key-value parirs, unordered, mutable
mydict = {
    'name': 'Shahriar',
    'age': 27,
    'city': 'dhaka'
}
print(mydict)

mydict2 = dict(name='Salpin', age=27, city='Kishoregang')
print(mydict2)

# access 
print(mydict['name'])

# add 
mydict['edu'] = 'CSE'
print(mydict)

# change 
mydict['edu'] = 'Computer Science and Engineering'
print(mydict)

# delete
del mydict['edu']
print(mydict)

# or 
mydict.pop('age')
print(mydict)

# or 
mydict.popitem() # last item remove
print(mydict)

# check
""" wrong code
if "name" in mydict:
    print('True')
print('False') # ?
"""

if "name" in mydict:
    print('True')
else:
    print('False')

# or 

try:
    print(mydict2['name'])
except:
    print('Error')


mydict = {
    'name': 'Shahriar',
    'age': 27,
    'city': 'dhaka'
}

print('\n')
# dict loop 

# keys
for key in mydict:
    print(key)

print('\n')
for key in mydict.keys():
    print(key)

# values
print('\n')
for value in mydict.values():
    print(value)

# key, val
print('\n')
for key, val in mydict.items():
    print(key, val)

# copy
mydict3 = mydict2 # it's not actual copy, if change original also change
print(mydict3)

mydict4 = mydict.copy() # dict(mydict)
print(mydict4)

mydict = {'name': 'shhariar', 'age': 27, 'email': 'cse.shahriar.hosen@gmail.com'}
mydict2 = dict(name='Salpin', age=27, city='Boston')

mydict2.update(mydict2) # values updated only key match
print(mydict2)


# tuple to dict
my_tuple = (9, 8)
mydict = {my_tuple: 15}
print(mydict)

# lsit to dict not posible
# my_tuple = [9, 8]
# mydict = {my_tuple: 15}
# print(mydict)


