from random import randint
import timeit

from bubble_sort import bubbleSort
from insertion_sort import insertionSort
from merge_sort import splitBeforeMerge
from tim_sort import timSort


def check_how_fast(function, element):
    return min(timeit.repeat(f'{function(element)}'))


if __name__ == "__main__":

    array = [randint(-100000, 100000) for i in range(5000)]

    #print(f'Unsorted list: {array}')

    list1 = array.copy()
    how_fast_1 = check_how_fast(bubbleSort, list1)

    #print(f'Bubble-sorted list: {list1} in {how_fast_1}')
    print(f'First: {list1[0]}, last: {list1[-1]}')
    print(f'Bubble sorted list in {how_fast_1}')

    list2 = array.copy()
    how_fast_2 = check_how_fast(insertionSort, list2)

    #print(f'Insertion-sorted list: {list2} in {how_fast_2}')
    print(f'First: {list2[0]}, last: {list2[-1]}')
    print(f'Insertion sorted list in {how_fast_2}')

    how_fast_3 = check_how_fast(splitBeforeMerge, array)
    list3 = splitBeforeMerge(array)

    #print(f'Merge-sorted list: {list3} in {how_fast_3}')
    print(f'First: {list3[0]}, last: {list3[-1]}')
    print(f'Merge sorted list in {how_fast_3}')

    how_fast_4 = check_how_fast(timSort, array)
    list4 = timSort(array)

    #print(f'Tim-sorted list: {list4} in {how_fast_4}')
    print(f'First: {list4[0]}, last: {list4[-1]}')
    print(f'Tim sorted list in {how_fast_4}')

    how_fast_5 = check_how_fast(sorted, array)
    list5 = sorted(array)

    #print(f'Python-sorted list: {list5} in {how_fast_5}')
    print(f'First: {list5[0]}, last: {list5[-1]}')
    print(f'Python sorted list in {how_fast_5}')
