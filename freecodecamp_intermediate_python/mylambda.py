# lambd arguments: expression
add10 = lambda x: x + 10 # x argument
print(add10(5))

mull = lambda x,y: x * y
print(mull(3,4))

# sorted 
pointers2D = [(1,2), (15, 1), (5, -1), (10, 4)]
pointers2D_sorted = sorted(pointers2D, key=lambda x: x[1]) # sort by second value
print(pointers2D_sorted)
pointers2D_sorted = sorted(pointers2D, key=lambda x: x[0] + x[1]) # sort by second value
print(pointers2D_sorted)

# map 