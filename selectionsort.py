from bublesort import make_population
from insertionsort import highlight


def selection_sort(array: list) -> list:
    sorted_array = array.copy()
    comparisions = 0
    swaps = 0
    begining = 0
    smallest, index = sorted_array[begining], begining

    while True:
        changed = False
        for i in range(begining, len(sorted_array)):
            if sorted_array[i] < smallest:
                print('O--', highlight(sorted_array, i))
                smallest, index = sorted_array[i], i
                changed = True
                comparisions += 1
        sorted_array.insert(begining, sorted_array.pop(index))
        print('<->', highlight(sorted_array, begining))
        swaps += 1
        begining += 1
        smallest, index = sorted_array[begining], begining

        if not changed:
            print(f'Total number of comparisons: {comparisions}')
            print(f'Total number of swaps: {swaps}')
            break

    return sorted_array


if __name__ == '__main__':
    pop = make_population(1, 1000, 25)
    sor = selection_sort(pop)
    print(sor)
