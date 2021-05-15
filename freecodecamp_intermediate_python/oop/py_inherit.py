# inherits, extend, override

class Employee: # base class
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f'{self.name} in working')

class SoftwareEngineer(Employee): # child class
    # override super __init__
    def __init__(self, name, age, salary, level): # # level only SoftwareEngineer class
        super().__init__(name, age, salary) # parent class initialize
        self.level = level # extend functionality

    def debug(self): # only for this class
        print(f'{self.name} is debugging...')

    # override
    def work(self):
        print(f'{self.name} in coding')


class Designer(Employee): # child class
    
    def draw(self):
        print(f'{self.name} is drawing...')
    
    # override
    def work(self):
        print(f'{self.name} in designing')


# instance
se = SoftwareEngineer('Shahriar', 28, 20000, 'Junior')
print(f'Name: {se.name} Age: {se.age}')
# se.work()
print(se.level) # level only work for software engineer
# se.debug()

d = Designer('Salpin', 28, 20000)
# d.work()
# d.draw()


# polymorphisom

# employees collection
employees = [
    SoftwareEngineer('Shahriar', 28, 20000, 'Junior'),
    SoftwareEngineer('Salpin', 28, 20000, 'Junior'),
    Designer('John', 28, 20000)
]

def motivate_employees(employees):
    for employee in employees:
        employee.work() # employee has many work, thant's is polymorphisom

motivate_employees(employees)

