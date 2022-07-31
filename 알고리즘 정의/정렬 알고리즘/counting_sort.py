import random


def counting_sort(array):
    count = [0] * (max(array) + 1)

    for item in array:
        count[item] += 1

    idx = 0
    for i in range(len(count)):
        for j in range(count[i]):
            array[idx] = i
            idx += 1
    return array


array = list(range(0, 21, 2))
random.shuffle(array)
print('origin list: {}'.format(array))
print('result list: {}'.format(counting_sort(array)))