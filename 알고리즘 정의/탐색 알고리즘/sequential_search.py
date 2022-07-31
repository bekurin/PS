import random


def sequential_search(array, target):
    for idx, item in enumerate(array):
        if item == target:
            return idx
    return -1


target = 5
array = list(range(21))
random.shuffle(array)
print('origin list: {}'.format(array))
print('target: {}, index: {}'.format(target, sequential_search(array, target)))