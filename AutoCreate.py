def create(name):
    with open(f'{name}.py', 'w'):
        pass


name = input('Enter py file name\n>>>')
create(name)
print(name, 'file created')
input('...')