import random

hash_table = [0 for _ in range(13)]


def hx(key):
    return key % 13


def fx(key):
    return 1 + key % 11


def hash_insert(hash_table, value):
    size = len(hash_table)
    index, fx_result, hx_result = 0, fx(value), hx(value)

    while index != size:
        temp = (hx_result + index * fx_result)
        if temp < size:
            if hash_table[temp] == 0:
                return temp
        else:
            if hash_table[temp % size] == 0:
                return temp % size
        index += 1
    return None


def hash_search(hash_table, value):
    size = len(hash_table)
    index, fx_result, hx_result = 0, fx(value), hx(value)

    while index != size:
        temp = (hx_result + index * fx_result)
        if temp < size:
            if hash_table[temp] == value:
                return temp
        else:
            if hash_table[temp % size] == value:
                return temp % size
        index += 1
    return None


array = list(range(3, 40, 3))
random.shuffle(array)
print('input list : {}'.format(array))
for item in array:
    index = hash_insert(hash_table, item)
    hash_table[index] = item
print('after input: {}'.format(hash_table))

array.reverse()
print('search list: {}'.format(array))
for item in array:
    index = hash_search(hash_table, item)
    print('search item: {:2}, index: {:2}'.format(item, index))
