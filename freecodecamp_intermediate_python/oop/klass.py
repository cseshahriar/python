""" 
Create Classes: class vs Instance
Function inside class
"""

# class
class SoftwareEngibeer:

    # class attributes
    alias = "Keyword Magician"


    def __init__(self, name, age, lavel, salary):
        # instance attributes
        self.name = name
        self.age = age
        self.level = lavel
        self.salary = salary


# instance
se1 = SoftwareEngibeer('Shahriar', 28, "Junior", 20000)

# access instance attributes
print(f'name: {se1.name}, age: {se1.age}, level: {se1.level}, salary: {se1.salary}')


# access class attributes
print(se1.alias)
print(SoftwareEngibeer.alias)
# print(SoftwareEngibeer.name) # can't