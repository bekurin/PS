# 프로그래머스 no.60062 외벽 점검
from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    
    answer = len(dist) + 1
    
    for i in range(length):
        for friends in permutations(dist, len(dist)):
            count = 1
            position = weak[i] + friends[count - 1]
            
            for j in range(i, i + length):
                if position < weak[j]:
                    count += 1
                    
                    if count > len(dist):
                        break
                    position = weak[j] + friends[count - 1]
            answer = min(answer, count)
    return answer if answer <= len(dist) else -1
