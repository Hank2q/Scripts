from bublesort import make_population
from time import perf_counter
from bublesort import conv_time
import shelve


def insertion_sort(array: list):
    iterations = 0
    swaps = 0
    checks = 0
    per_iter = 0
    sorted_array = array.copy()
    for i in range(1, len(sorted_array)):
        iterations += 1
        # print(highlight(sorted_array, i), 'checking', end='\r')
        element = sorted_array[i]
        j = i-1
        while element < sorted_array[j] and j >= 0:
            checks += 1
            per_iter += 1
            sorted_array.insert(j, sorted_array.pop(i))
            # print(highlight(sorted_array, j), 'swapping', end='\r')
            swaps += 1
            i = j
            j -= 1
        print(f'checks in itteration {iterations} is {per_iter}')
        per_iter = 0
    # print(f'total swaps: {swaps}')
    # print(f'total checks: {checks}')
    print(f'total itterations: {iterations}')
    return sorted_array


def highlight(array, i):
    copy = array.copy()
    copy[i] = [copy[i]]
    return copy


if __name__ == '__main__':
    # pop = make_population(1,199, 25)
    # x = insertion_sort(pop)
    # print(pop)
    # print('\a')
    for i in range(30):
        pop = [i for i in range(i, 0, -1)]
        # print(pop)
        print()
        print(f'n is {len(pop)}')
        insertion_sort(pop)