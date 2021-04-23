# Python learning repository

## Strings: ordered, immutable, text representation
<pre>
my_string = "Hello World"
print(my_string)

my_string = 'I\'m a programmer'
print(my_string)

my_string = "I'm a programmer"
print(my_string)

my_string = """ I'm a 
programmer"""
print(my_string)

my_string = "Helllo World"
char = my_string[0]
print(char)
</pre>

## string object does not support iitem assignment

### substring 
<pre>
substring = my_string[1:5] # start:stop
print(substring)

substring = my_string[:5] # start begaining to stop
print(substring)

substring = my_string[2:] # start postion 2 to end
print(substring)

substring = my_string[::2] # step(every second char)
print(substring)

greeting = "Hello"
name = "tom"
sentance = greeting + ' ' +name
print(sentance)
</pre>

### loop
<pre>
for i in sentance:
    print(i)    
</re>

## heck 
<pre>
if 'e' in sentance:
    print('True')
else:
    print('False')
</re>

##usefull methods
<pre>
my_string = '    Hello World  '
print(my_string)
</re>

## emove whitespace
<pre>
my_string = my_string.strip() # not change original str
print(my_string)
</re>

## pper
<pre>
my_string = 'hellow world'
upper_str = my_string.upper()
print(upper_str)
print(upper_str.lower())
</pre>

## startwith, endswith
<pre>
print(my_string.startswith('hello'))
print(my_string.endswith('world'))
</pre>

## find
<pre>
find_str = my_string.find('lo') # return postion
print(find_str)
</pre>

## count
<pre>
count_str = my_string.count('o') # how many o
print(count_str)
</pre>

## replace 
<pre>
replace_str = my_string.replace('world', 'Universe')
print(replace_str)

my_string = 'how are you doing'
my_list = my_string.split() # str to list, split by space
print(my_list)

my_string = 'how,are,you,doing'
my_list = my_string.split(",") # split by comma
print(my_list)
</pre>

## list to str
<pre>
my_str = ' '.join(my_list)
print(my_str)
</pre>

## list tricks
<pre>
my_list = ['a'] * 1000000
</pre>

## check time complexity
<pre>
from timeit import default_timer as timer
</pre>

## bad code
<pre>
start = timer()
my_string = ''
for i in my_list:
    my_string += i

stop = timer()
print(stop - start) # 0.2591306699998768
</pre>

### good 
<pre>
start = timer()
my_string = ''.join(my_list)
stop = timer()
print(stop - start) # 0.2591306699998768
</pre>

## formate : %s, format(), f-string

## str
<pre>
var = "Tom"
my_string = "the variable is %s" % var
print (my_string)
</pre>

## int
<pre>
var = 3
my_string = "the variable is %d" % var
print (my_string)

var = 3.333 # 3.333000 is floate 
my_string = "the variable is %.2f" % var
print (my_string)
</pre>

## format()
<pre>
var = 3.434
var2 = 4
my_string = 'the variable is {:.2f} and {}'.format(var, var2)
print(my_string)
</pre>

# f-strings (recommand)
<pre>
print(f' the variable is {var} and {var2}')
</pre>
