 # Generator is a simple way of creating iterators
def fib():
    a, b = 0, 1
    while True:
        """ 
        yield statement pauses the function saving all its states 
        and later continues from there on successive calls.
        """
        yield a
        a, b = b, a + b


for f in fib():
    if f > 5:
        break
    print(f)