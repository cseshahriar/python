# Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
a = "Hello"
print(a)

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Strings are Arrays
a = "Hello, World!"
print(a[1])

# looping
for x in "banana":
    print(x)

# String Length
a = "Hello, World!"
print(len(a))

# Check String
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("Yes, 'expensive' is NOT present.")
