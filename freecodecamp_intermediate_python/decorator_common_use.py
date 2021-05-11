import time 

def time_it(func): 
    def inner(*args, **kwargs): 
        t = time.time()
        result = func(*args, **kwargs)
        print (func.__name__ + " takes " +  str(time.time() - t) + " seconds.")
        return result 
    return inner

@time_it
def add_stuff(x,y): return x+y

add_stuff(1,2)


def add_logs(f): 
    def inner(*args, **kwargs): 
        # insert real logging code here 
        print('write', *args, "to file")
        return f(*args, **kwargs)
    return inner    

@add_logs
def add_things(x,y,z): return x+y+z
add_things(1,4,3)

def once_per_min(f): 
    calltime = 0 
    def inner(*args, **kwargs): 
        nonlocal calltime
        gap = time.time() - calltime
        if gap < 60: 
            msg = "You're calling this function too often. Try again in " + \
                          str(60 - gap) + " seconds."
            raise Exception(msg)
        calltime = time.time()
        return f(*args, **kwargs)
    return inner

@once_per_min
def add_stuff(x,y,z): return x+y+z
add_stuff(1,2,4)