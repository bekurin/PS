# 프로그래머스 No.42747 H-Index

def solution(citations):
    answer = 0
    citations.sort(reverse=True)

    for h_idx, citation in enumerate(citations):
        answer = max(answer, min(citation, h_idx + 1))
    return answer


citations = [3, 0, 6, 1, 5]
print(solution(citations))
