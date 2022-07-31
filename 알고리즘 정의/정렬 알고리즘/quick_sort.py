import random


def quick_sort(array, left, right):
    if left > right: return
    pivot = partition(array, left, right)
    quick_sort(array, left, pivot - 1)
    quick_sort(array, pivot + 1, right)


def partition(array, left, right):
    pivot, i = array[right], left - 1
    for j in range(left, right):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1


array = list(range(21))
random.shuffle(array)
print('origin list: {}'.format(array))
quick_sort(array, 0, len(array) - 1)
print('result list: {}'.format(array))
