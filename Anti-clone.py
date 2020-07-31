import os
import send2trash
from concurrent.futures import ThreadPoolExecutor
from time import perf_counter


def move_files(alist):
    for value in range(1, len(alist)):
        old = '.\\' + alist[value]
        folder, file = os.path.split(old)
        parent_folder, f = os.path.split(folder)
        # dup_folder = folder + '\\duplicates\\' if want to put each dup in its containing dir
        dup_folder = '.\\duplicates\\' + f + '\\'  # gather all dups in one folder
        dup_name = '[' + os.path.split(alist[0])[-1] + ']' + f' dup({value}) {file}'
        new = dup_folder + dup_name
        try:
            os.rename(old, new)
        except FileNotFoundError:
            os.mkdir(dup_folder)
            os.rename(old, new)


def move_del(d):
    delete = input('Delete duplicates? (Y/N)')
    if delete.lower().startswith('y'):
        for values in d.values():
            with ThreadPoolExecutor() as exe:
                exe.map(send2trash.send2trash, values[1:])
        print('\n***Duplicates Deleted***\n')
    else:
        move = input('Move duplicates to separate folder? (Y/N)')
        if move.lower().startswith('y'):
            try:
                os.mkdir('.\\duplicates')
            except FileExistsError:
                pass
            with ThreadPoolExecutor() as exe:
                exe.map(move_files, d.values())
            print('\n***Duplicates moved to "duplicates" folders***\n')


def get_hex(string):
    return hex(int(f'0x{string}', 16))


def checksum(filename, alg='SHA256'):
    cmd = 'certutil -hashfile'
    try:
        sumed = get_hex(os.popen(f'{cmd} "{filename}" {alg}').readlines()[1])
    except ValueError:
        return
    return sumed


def all_or_one(d, path, file):
    name = os.path.join(path, file)
    sumx = checksum(name)
    in_dir = os.path.relpath(name)
    if sumx:
        if sumx in d:
            d[sumx].append(in_dir)
        else:
            d[sumx] = [in_dir]


def store_sum(dire, ext):
    d = {}
    if ext == 'all' or ext == '':
        for path, dirs, files in os.walk(dire):
            for file in files:
                all_or_one(d, path, file)
        return d
    else:
        for path, dirs, files in os.walk(dire):
            for file in files:
                if file.endswith(ext):
                    all_or_one(d, path, file)
        return d


def check_dups(dic, show=False):
    dups = False
    dups_cash = {}
    un = 0
    on = 0
    for k, v in dic.items():
        if len(v) > 1:
            dups = True
            dups_cash[k] = v
            un += len(v) - 1
            on += len(v)
            if show:
                for val in v:
                    print(val, '\n')
                print('have the same sum : ', k, '\n'+'_'*60, '\n')
    if dups:
        on -= un
        print(f'Total unwanted files: {un}\nOriginal number of files: {on}')
        move_del(dups_cash)
    else:
        print('***No duplicates found***')


def main():
    directory = input('Drag folder here or paste the name\n>>>').strip('"')
    os.chdir(directory)
    extension = input('what file type to check (txt, pdf, mp3 or all)\n>>>')
    check_dups(store_sum(directory, extension))
    input('\n\n\nPress Enter to close......')


if __name__ == '__main__':
    start = perf_counter()
    main()
    end = perf_counter()
    print(f'Time to finish: {round(end-start,2)}')