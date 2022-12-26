from random import randint
from timeit import repeat
from bubble_sort import bubbleSort
from insertion_sort import insertionSort
from merge_sort import splitBeforeMerge

def check_how_fast(function, element):
    pass


if __name__ == "__main__":

    array = [randint(1, 1000) for i in range(1000)]

    print(f'Unsorted list: {array}')

    list1 = array
    bubbleSort(list1)

    print(f'Bubble-sorted list: {list1}')

    list2 = array
    insertionSort(list2)

    print(f'Insertion-sorted list: {list2}')

    list3 = splitBeforeMerge(array)

    print(f'Merge-sorted list: {list3}')
