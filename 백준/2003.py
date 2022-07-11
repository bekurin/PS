# 백준 No.2003 수들의 합 2

n, m = map(int, input().split())
data_list = list(map(int, input().split()))

def solution(data_list, n, m):
    target = sum(data_list)

    if target == m:
        return 1
    elif target < m:
        return 0
    else:
        return two_pointer(data_list, n, m)

def two_pointer(data_list, n, m):
    answer = 0
    total, right = 0, 0

    for left in range(n):
        while total < m and right < n:
            total += data_list[right]
            right += 1
        if total == m:
            answer += 1
        total -= data_list[left]
    return answer

print(solution(data_list, n, m))