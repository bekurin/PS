import random


def hx(key):
    return key % 29


def fx(key):
    return 1 + key % 23


def hash_insert(hash_table, value):
    size = len(hash_table)
    index, fx_result, hx_result = 0, fx(value), hx(value)

    while index != size:
        temp = (hx_result + index * fx_result) % size
        if hash_table[temp] == 0:
            return temp
        index += 1
    return None


def hash_search(hash_table, value):
    size = len(hash_table)
    index, fx_result, hx_result = 0, fx(value), hx(value)
    while index != size:
        temp = (hx_result + index * fx_result) % size
        if hash_table[temp] == value:
            return temp
        index += 1
    return None


hash_size = 30
hash_table = [0 for _ in range(hash_size)]

array = list(range(3, 93, 3))
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
