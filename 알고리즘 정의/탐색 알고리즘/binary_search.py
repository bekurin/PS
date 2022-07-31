
def recursion_binary_search(array, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return recursion_binary_search(array, target, left, mid - 1)
    else:
        return recursion_binary_search(array, target, mid + 1, right)


def loop_binary_search(array, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


array = list(range(21))
target = array[8]
print('origin list: {}'.format(array))
print('recursion target: {}, index = {}'.format(target, recursion_binary_search(array, target, 0, len(array))))
print('loop      target: {}, index = {}'.format(target, loop_binary_search(array, target, 0, len(array))))
