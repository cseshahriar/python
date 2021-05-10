# Json: javascript object notation
""" 
Python-----------Json
dict------------object
list,tuple------array
str-------------string
int,long,float---number
True-------------true
False------------false
None-------------null
"""
import json

# dict
person = {
    "first_name": "Shahriar",
    "last_name": "Hosen",
    "hobbies": ["running", "swimming", "singing"],
    "age": 28,
    "hasChildren": False,
    "titles": ["Engineer", "Programmer"]
}

# py dict to json(serialization or encoding)
personJson = json.dumps(person, indent=4, sort_keys=True) # separators=('; ', '= ')
print(personJson)