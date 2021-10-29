# 프로그래머스 no.42586 기능개발
import math

def solution(progresses, speeds):
  answer, days = [], []
  index, position, count = 0, 0, 0

  for progress in progresses:
    days.append(math.ceil((100-progress)/speeds[index]))
    index += 1
  
  while(position < len(days)):
    count = 0
    day = days[position]
    
    for i in range(position, len(days)):
      if day >= days[position]:
        position += 1
        count += 1
      else:
        break
    answer.append(count)
  return answer

progresses = [93,30,55]
speeds = [1, 30 ,5]
print(solution(progresses, speeds))