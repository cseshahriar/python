def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am a ordinary")

ordinary()

def make_divide(func):
    def inner(a, b):
        print("I am going to divide", a, " and ", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a,b)
    return inner

@make_divide # checking if divide by zero
def divide(a, b):
    print(a/b)

divide(10, 3) # 10/3


def start(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@start
@percent
def printer(msg):
    print(msg)

printer("Hello")