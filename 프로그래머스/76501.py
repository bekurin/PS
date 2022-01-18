# 프로그래머스 No.76501 음양 더하기
def solution(absolutes, signs):
  answer = 0
  for i, number in enumerate(absolutes):
    if signs[i]:
      answer += number
    else:
      answer -= number
  return answer

absolutes = [4,7,12]
signs = [True,False,True]
print(solution(absolutes, signs))