# Context manager
class ManagedFile:
    """ content manager """    
    def __init__(self, filename):
        print('init')
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, trace):
        if self.file:
            self.file.close()
        print('exit')

with ManagedFile('notes.txt') as file:
    print('do something')
    file.write('some todo...')