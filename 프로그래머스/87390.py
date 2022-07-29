# 프로그래머스 No.87390 n^2 배열 자르기

def solution(n, left, right):
    answer = []
    for idx in range(left, right + 1):
        answer.append(max(divmod(idx, n)) + 1)
    return answer

n, left, right = 3, 2, 5
print(solution(n, left, right))
