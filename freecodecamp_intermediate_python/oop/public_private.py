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
        # it's can't access outside of class that's call encapsulation 

    def code(self):
        self.__num_bugs_solved += 1
    
    # setter methods
    def set_salary(self, base_value):
        # check value, enforce constructor
        self._salary = self._calculate__salary(base_value)

    def set_num_bugs_solved(self, value):
        self.__num_bugs_solved = value

    # gette methods
    def get_salary(self): 
        return self._salary

    def get_num_bugs_solved(self): 
        return self.__num_bugs_solved

    def _calculate__salary(self, base_value):
        if self.__num_bugs_solved < 10:
            return base_value
        if self.__num_bugs_solved < 100:
            return base_value * 2
        return base_value * 3


se = SoftwareEngineer('Shahriar', 28)
print(f'{se.name} {se.age}')

print(f'{se._salary}')
# print(f'{se._salary} {se._num_bugs_solved}') # can't access
se.set_salary(10000)
print(se.get_salary())

se.set_num_bugs_solved(20000)
print(se.get_num_bugs_solved())

for i in range(70):
    se.code()

# print(se.__num_bugs_solved) # we can't access outside of class it's call encapsulation
print(se.get_salary())
