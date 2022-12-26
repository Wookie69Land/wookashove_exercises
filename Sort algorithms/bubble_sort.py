import random


def bubbleSort(array_of_nr):

    n = len(array_of_nr) - 1
    swapped = False

    for i in range(n):
        for j in range(0, n-i):

            if array_of_nr[j] > array_of_nr[j+1]:
                array_of_nr[j], array_of_nr[j+1] = array_of_nr[j+1], array_of_nr[j]
                swapped = True

        if not swapped:
            break


if __name__ == "__main__":

    list = []
    for i in range(random.randint(5, 20)):
        list.append(random.randint(1, 100))

    print(f'Unsorted list: {list}')

    bubbleSort(list)

    print(f'Sorted list: {list}')
