print("Hello World")
print('Hello World')

a = "Hello"

b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print(b)
print(b[1])

# str looping 
for i in b:
    print(i)

# str length 
print(len(a))

# str checking 
txt = 'The best things in life are free'
print("free" in txt)

if "free" in txt:
    print("Yes, 'free' is present.")


print("expensive" not in txt)
if "expensive" not in txt:
    print("Yes 'expensive' is not present.")

# slicing 
# Get the characters from position 2 to position 5 (not included):
b = "Hello, World"
print(b[2:5]) # start  and end index 

# Slice From the Start
print(b[:5])

# Slice To the End
print(b[2:])

# Negative Indexing
print(b[-5:-2])

a = "Hello World!"
print(a.upper())
print(a.lower())


# remove whitespaces 
a = " Hello, World!"
print(a.strip())

# Replace String
print(a.replace("H", 'J'))

# Split String
print(a.split(",")) # return list