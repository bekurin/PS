# 프로그래머스 No.17681 [1차] 비밀지도

def get_binary_list(number, n):
    base = ''
    while number > 0:
        number, mode = divmod(number, 2)
        base += str(mode)

    if len(base) < n:
        base += '0' * (n - len(base))
    return list(base[::-1])


def solution(n, arr1, arr2):
    answer = []
    arr1_map_list = get_map_list(n, arr1)
    arr2_map_list = get_map_list(n, arr2)

    for x in range(n):
        temp = ''
        for y in range(n):
            temp += '#' if arr1_map_list[x][y] or arr2_map_list[x][y] else ' '
        answer.append(temp)
    return answer


def get_map_list(n, array):
    map_list = []
    for number in array:
        map_list.append(list(map(int, get_binary_list(number, n))))
    return map_list


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))
