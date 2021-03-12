import json

books = {}
books['tom'] = {
    'name': 'tom',
    'address': '1 red street, NY',
    'phone': 98989898
}

books['bob'] = {
    'name': 'bob',
    'address': '2 red street, NY',
    'phone': 99989898
}

# convert to json
json_str = json.dumps(books)
print(json_str)

# write file
# with open("/home/shosen/projects/python/codebasics/books.txt", "w") as file:
#     file.write(json_str)

# reading 
with open("/home/shosen/projects/python/codebasics/books.txt", "r") as file:
    file.read()