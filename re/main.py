import re

test_string = "123abc456789abc123ABC"

# case sensitive
# find pattern
# pattern = re.compile(r"abc") # raw string
# matches = pattern.finditer(test_string)

# match(), search(), findall()
# matches = re.finditer('abc', test_string)
# matches = re.findall('abc', test_string)
matche = re.match('123', test_string) # matche are find at the beginning
print(matche)
# for match in matches:
#     print(match) # abc abc


# a = r"\tHello" # raw string
# print(a)