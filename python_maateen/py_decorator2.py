from time import time

def timer(function):
    
    def count_time():
        start = time()
        function() # received func call
        stop = time()
        print(stop - start, 'seconds')
        return 
    
    return count_time


@timer
def hello():
    print('Hello World')
    return

@timer
def another_function():
    for item in [1, 2, 3,4,5]:
        print(item)
    return

hello()
another_function()

# builtin decorator: @classmethod
class MyClass:

    def __init__(self):
        pass

    def square(self, x):
        return x**2

    @classmethod # অবজেক্ট তৈরি না করেও কল করা যায়।
    def cube(self, x):
        return x**3


# builtin decorator: @property
class MyClass2: 

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

        
if __name__ == "__main__":
    myclass = MyClass()
    # obj
    print(myclass.square(3))
    print(myclass.cube(3))
    
    # class
    print(MyClass.cube(3))

    myclass2 = MyClass2('Shahriar', 'Hosen')
    print(myclass2.full_name)