import random


def heap_sort(array):
    n = len(array)
    build_heap(array, n)
    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, 0, i)


def build_heap(array, n):
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, i, n)


def heapify(array, k, n):
    left, right, temp = 2 * k + 1, 2 * k + 2, k

    if left < n and array[temp] < array[left]:
        temp = left

    if right < n and array[temp] < array[right]:
        temp = right

    if array[k] < array[temp]:
        array[temp], array[k] = array[k], array[temp]
        heapify(array, temp, n)


array = list(range(0, 21, 2))
random.shuffle(array)
print('origin list: {}'.format(array))
heap_sort(array)
print('result list: {}'.format(array))
