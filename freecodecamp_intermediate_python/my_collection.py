# collection: Counter, namedtuple, OrderedDict, defaultdict, dque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# counter
a = "dfdfdfdfdfdfd"
my_counter = Counter(a)
print(my_counter) # ({'d': 7, 'f': 6})
print(my_counter.items()) 
print(my_counter.keys()) 
print(my_counter.values()) 
print(my_counter.most_common(1)[0][0]) # most common element
print(list(my_counter.elements())) 


# namedtuple
Point = namedtuple('Point', 'x,y') # class, fields
pt = Point(1,-4) # object with values pass to constructor
print(pt) # namedtuple
print(pt.x, pt.y) # namedtuple


# OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

# defaultdict
d = defaultdict(int) # dafault type
d['a'] = 10
d['b'] = 15
print(d['b'])
print(d['c']) # return default val int (0)

# deque
my_deque = deque()
my_deque.append(1)
my_deque.append(2)
my_deque.appendleft(3)
print(my_deque) # deque([3, 1, 2])
my_deque.pop()
print(my_deque) # pop from last
my_deque.popleft()
print(my_deque) # pop from first
my_deque.clear()
print(my_deque) 
my_deque.extend([1,2,3,4,5])
print(my_deque) 
my_deque.extendleft([1,2,3,4,5])
print(my_deque) 
my_deque.rotate(2)
print(my_deque) 