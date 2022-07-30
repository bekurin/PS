import random


def insertion_sort(array):
    for i in range(1, len(array)):
        prev = i - 1
        new_item = array[i]
        while prev >= 0 and new_item < array[prev]:
            array[prev + 1] = array[prev]
            prev -= 1
        array[prev + 1] = new_item
    return array


array = list(range(11))
random.shuffle(array)
print('origin list: {}'.format(array))
print('result list: {}'.format(insertion_sort(array)))
