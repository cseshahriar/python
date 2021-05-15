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

    # instance methods
    def code(self):
        print(f'{self.name} writing code...')

    def code_in_languages(self, language):
        print(f'{self.name} is writing code in {language}')

    # special methods(every object already has that or builtin)
    # dunder methods
    def __str__(self):
        info = f'name = {self.name}, age = {self.age}, level = {self.level}, salary = {self.salary}'
        return info

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


# instance
se1 = SoftwareEngibeer('Shahriar', 28, "Junior", 20000)
se2 = SoftwareEngibeer('Shahriar', 28, "Junior", 20000)

# access instance attributes
print(f'name: {se1.name}, age: {se1.age}, level: {se1.level}, salary: {se1.salary}')


# access class attributes
print(se1.alias)
print(SoftwareEngibeer.alias)
# print(SoftwareEngibeer.name) # can't

print(se1)
se1.code()
se1.code_in_languages('Python')

print(se1 == se2) # true