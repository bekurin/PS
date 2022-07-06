# 백준 No.1806 부분합
def solution(n, s, numbers):
    target = sum(numbers)

    if target == s:
        return n
    elif target < s:
        return 0
    elif target > s:
        return two_pointer(n, s, numbers)


def two_pointer(n, s, numbers):
    answer = 1000000001
    total, right = 0, 0
    for left in range(n):
        while total < s and right < n:
            total += numbers[right]
            right += 1
        if total >= s:
            answer = min(answer, right - left)
        total -= numbers[left]
    return answer


n, s = map(int, input().split())
numbers = list(map(int, input().split()))
print(solution(n, s, numbers))
