from random import randint


def quickSort(list):

    if len(list) < 2:
        return list

    lower, same, higher = [], [], []

    pivot = list[randint(0, len(list) - 1)]

    for element in list:
        if element < pivot:
            lower.append(element)
        elif element == pivot:
            same.append(element)
        elif element > pivot:
            higher.append(element)

    return quickSort(lower) + same + quickSort(higher)


if __name__ == "__main__":

    list = [randint(1, 1000) for i in range(randint(5, 20))]

    print(f'Unsorted list: {list}')

    sorted_list = quickSort(list)

    print(f'Sorted list: {sorted_list}')