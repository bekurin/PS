# 프로그래머스 no.12979 기지국 설치
def solution(n, stations, w):
    answer, location, index = 0, 1, 0
    
    while location <= n:
        if index < len(stations) and location >= stations[index] - w:
            location = stations[index] + w + 1
            index += 1
        else:
            location += 2 * w + 1
            answer += 1
    return answer
