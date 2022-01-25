# 프로그래머스 No.12903 가운데 글자 가져오기

def solution(s):
    middle = len(s) // 2
    return s[middle-1] + s[middle] if len(s) % 2 == 0 else s[middle]

s = "abcde"
print(solution(s))
