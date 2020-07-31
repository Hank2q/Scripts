from random import randint
import shelve
from time import perf_counter


def conv_time(secs):
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    return f'{hours}h:{mins}m:{secs}s'


def make_population(low, hi, n):
    return [randint(low, hi) for i in range(n)]


def bubble_sort(array):
    sorted_array = array.copy()
    total_runs = 0
    swaps = 0
    while True:
        changed = False
        for i1 in range(len(sorted_array) - 1):
            i2 = i1 + 1
            print(highlight(sorted_array, i1), 'Checking', sep='--->')
            if sorted_array[i1] > sorted_array[i2]:
                sorted_array[i1], sorted_array[i2] = sorted_array[i2], sorted_array[i1]
                changed = True
                print(highlight(sorted_array, i1), 'Swapped', sep='--->')
                swaps += 1
        # print()
        total_runs += 1
        if not changed:
            print(f'Total iterations: {total_runs}')
            print(f'Number of swaps: {swaps}')
            print()
            break
    return sorted_array


def highlight(array, i):
    copy = array.copy()
    copy[i] = copy[i], copy[i + 1]
    copy.pop(i + 1)
    return copy


if __name__ == '__main__':
    pop = make_population(1, 1000, 20)
    start = perf_counter()
    x = bubble_sort(pop)
    stop = perf_counter()
    print(f'time to sort: {conv_time(stop-start)}')
