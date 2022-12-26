from random import randint
from merge_sort import mergeSort


def modified_insertionSort(list, left=0, right=None):

    if right is None:
        right = len(list) - 1

    for i in range(left + 1, right + 1):
        number = list[i]
        j = i - 1

        while j >= left and list[j] > number:
            list[j+1] = list[j]
            j -= 1

        list[j+1] = number

    return list


def timSort(list):
    min_run = 32
    length = len(list)

    for i in range(0, length, min_run):
        modified_insertionSort(list, i, min((i + min_run - 1), length - 1))

    size = min_run
    while size < length:
        for start in range(0, length, size*2):
            middle = start + size - 1
            end = min((start + size * 2 - 1), (length - 1))

            merged_list = mergeSort(list1=list[start:middle + 1],
                                    list2=list[middle + 1:end + 1])

            list[start:start + len(merged_list)] = merged_list

        size *= 2

    return list


if __name__ == "__main__":

    list = [randint(1, 1000) for i in range(randint(64, 128))]

    print(f'Unsorted list: {list}')

    list2 = timSort(list)

    print(f'Sorted list: {list2}')