import os
from pyunpack import Archive


def make_folder(dir_name):
    folder = dir_name + ' Folder'
    try:
        os.mkdir(folder)
    except FileExistsError:
        pass
    return folder


dir = 'C:\\Users\\HANK\\Downloads'
os.chdir(dir)
extensions = ['zip', 'rar', '7z']


for file in os.listdir('.'):
    if os.path.isfile(file):
        name, ext = os.path.splitext(file)
        if ext.strip('.') in extensions:
            print(file)
            name = make_folder(name.upper())
            f = Archive(file)
            f.extractall(name)
            os.rename(file, f'{name}/{file}')
