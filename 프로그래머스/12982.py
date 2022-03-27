# 프로그래머스 No.12982 예산
def solution(d, budget):
  answer = 0
  d.sort()
  for item in d:
    if budget >= item:
      budget -= item
      answer += 1  
  return answer

d = [1,3,2,5,4]
budget = 9
print(solution(d, budget))