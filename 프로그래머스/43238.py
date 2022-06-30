# 프로그래머스 No.43238 입국심사
def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n

    while left <= right:
        mid = (left + right) // 2
        immigration = 0

        for time in times:
            immigration += mid // time
            if immigration >= n:
                break

        if immigration >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

n = 6
times = [7, 10]
print(solution(n, times))