# 프로그래머스 No.42587 프린터
def solution(priorities, location):
  answer = []

  if len(priorities) == 1:
    return 1
  
  ordered_priorities = [(idx, priority) for idx, priority in enumerate(priorities)]

  while ordered_priorities:
    candidate = ordered_priorities.pop(0)
    if not ordered_priorities:
      answer.append(candidate)
      break

    if candidate[-1] < max(ordered_priorities, key = lambda x: x[-1])[-1]:
      ordered_priorities.append(candidate)
    else:
      answer.append(candidate)
      
  for idx, item in enumerate(answer):
    if item[0] == location:
      return idx + 1

priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))
    
    
