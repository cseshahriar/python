# file handling
try:
    with open('test.txt', 'r') as my_file:
        content = my_file.read()
        print(content)
except:
    print('The file does not exist.')

# loop index except handling
try:
    my_list = []
    print(my_list[0])
except IndexError as e:
    print(e)

# i/o error handling
try:
    my_file = open('test.txt')
    content = my_file.read()
    i = int(content.strip())

except IOError as e:
    errno, strerror = e.args
    print("I/O error({0}): {1}".format(errno, strerror))

except ValueError:
    print("No valid integer in line.")

except:
    print("Unexpected error!")


# many exception
try:
    my_file = open('test.txt')
    content = my_file.read()
    i = int(content.strip())

except (IOError, ValueError):
    pass


# try except else 
try:
    a = 5
    b = 8
    print(a + b)
except ValueError as e:
    print(e)
else:
    print('There is no exception.')


# try except finally
try:
    with open('test.txt', 'r') as my_file:
        content = my_file.read()
        print(content)
except FileNotFoundError:
    print('The file does not exists.')
finally:
    print('To be or not be that is the question.')


# raise Exception
try:
    raise NameError('Hey! It is a custom error message.')
except NameError as e:
    print(e)
