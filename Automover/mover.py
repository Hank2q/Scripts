import filetype
import os
import sys


def move(source, destination, file):
    new_name = os.path.join(destination, file)
    try:
        os.rename(source, new_name)
    except FileExistsError:
        count = 1
        name, ext = os.path.splitext(file)
        file = f'{name} {str(count)}{ext}'
        new_name = os.path.join(destination, file)
        file_exist = os.path.exists(new_name)
        while file_exist:
            count += 1
            file = f'{name} {str(count)}{ext}'
            new_name = os.path.join(destination, file)
            file_exist = os.path.exists(new_name)
        os.rename(source, new_name)


def mover(target_path):
    videos_dir = r'C:\Users\HASSANIN\Videos'
    audio_dir = r'C:\Users\HASSANIN\Music'
    pictures_dir = r'C:\Users\HASSANIN\Pictures'
    docs_dir = r'C:\Users\HASSANIN\Documents'
    docs = ['Presentation', 'Spreadsheet', 'Doctumen']
    for file in os.listdir(target_path):
        full_name = os.path.join(target_path, file)
        file_type = filetype.guess(file)
        if file_type in docs:
            move(full_name, docs_dir, file)
        elif file_type == 'Audio':
            move(full_name, audio_dir, file)
        elif file_type == 'Image':
            move(full_name, pictures_dir, file)
        elif file_type == 'Video':
            move(full_name, videos_dir, file)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        mover(sys.argv[1])
    else:
        mover(input('Enter folder name:\n>>> '))
