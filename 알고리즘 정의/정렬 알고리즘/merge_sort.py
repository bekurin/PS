import random

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(array, left, right)


def merge(array, left, right):

    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        k, i = k + 1, i + 1
    while j < len(right):
        array[k] = right[j]
        k, j = k + 1, j + 1
    return array


array = list(range(11))
random.shuffle(array)
print('origin list: {}'.format(array))
print('result list: {}'.format(merge_sort(array)))