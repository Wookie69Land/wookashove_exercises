from random import randint


def mergeSort(list1, list2):

    if len(list1) == 0:
        return list2

    if len(list2) == 0:
        return list1

    result = []
    index_1 = index_2 = 0

    while len(result) < len(list1) + len(list2):
        if list1[index_1] <= list2[index_2]:
            result.append(list1[index_1])
            index_1 += 1
        else:
            result.append((list2[index_2]))
            index_2 += 1

        if index_2 == len(list2):
            result += list1[index_1:]
            break

        if index_1 == len(list1):
            result += list2[index_2:]
            break

    return result


def splitBeforeMerge(list):

    if len(list) < 2:
        return list

    middle = len(list) // 2

    return mergeSort(list1=splitBeforeMerge(list[:middle]),
                     list2=splitBeforeMerge(list[middle:]))


if __name__ == "__main__":

    list = [randint(1, 1000) for i in range(randint(5, 20))]

    print(f'Unsorted list: {list}')

    sorted_list = splitBeforeMerge(list)

    print(f'Sorted list: {sorted_list}')
