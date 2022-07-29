import random


def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


array = list(range(21))
random.shuffle(array)
print('origin list: {}'.format(array))
print('result list: {}'.format(bubble_sort(array)))