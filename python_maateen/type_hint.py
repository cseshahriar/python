def add(a: int, b:int) -> int: #
    """
    a, b is type int
    return type also int
    """
    c = a + b
    return c

print(add(2,3))


def add2(a:int, b:int) -> int:
    print(a, type(a))
    print(b, type(b))
    c = a + b
    print(c, type(c))
    return c

print(add2(2,4))

# !
def add3(a: int, b: int) -> int:
    print(a, type(a))
    print(b, type(b))
    c = a + b
    print(c, type(c))
    return c

add3('Bangla', 'desh')