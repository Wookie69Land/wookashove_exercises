from random import randint


def insertionSort(list):

    for i in range(1, len(list)):
        number = list[i]
        j = i - 1

        while j >= 0 and list[j] > number:
            list[j+1] = list[j]
            j -= 1

        list[j+1] = number

    return list


if __name__ == "__main__":

    list = [randint(1, 1000) for i in range(randint(5, 20))]

    print(f'Unsorted list: {list}')

    insertionSort(list)

    print(f'Sorted list: {list}')