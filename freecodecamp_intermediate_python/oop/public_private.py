# access modifiers

class SoftwareEngineer:

    def __init__(self, name, age):
        # public instance attributes
        self.name = name
        self.age = age
        # protected instance attributes: same class and child class can access
        self._salary = None
        # private instance attributes
        self.__num_bugs_solved = 0 # private: only inside class access can access

    def get_salary(self): 
        return self._salary

    def get_num_bugs_solved(self): 
        return self.__num_bugs_solved


se = SoftwareEngineer('Shahriar', 28)
print(f'{se.name} {se.age}')

print(f'{se._salary}')
# print(f'{se._salary} {se._num_bugs_solved}') # can't access
print(se.get_salary())
print(se.get_num_bugs_solved())

