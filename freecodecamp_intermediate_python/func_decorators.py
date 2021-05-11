# Decorators: pwowerful tools, func, cls decorators
import functools

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr+kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returened {result}")
        return result
    return wrapper


# func decorators
def my_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # do something before
        result = func(*args, **kwargs)
        # do something after
        return result
    return wrapper

# uses 
@my_decorator
def add5(x):
    return x + 5

print(add5(10))

# another example 
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


# uses
@debug
@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}')

greet('Shahriar')


