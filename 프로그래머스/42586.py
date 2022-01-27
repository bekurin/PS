# 프로그래머스 no.42586 기능개발 구현 코드
import math

def solution(progresses, speeds):
  answer, days = [], []
  position, count = 0, 0

  days = list(map(lambda x: math.ceil((100-progresses[x]) / speeds[x]), range(len(progresses))))
  
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


# 프로그래머스 no.42586 기능개발 리팩토링
def initDays(progresses, speeds):
  days = list(map(lambda x: math.ceil((100-progresses[x]) / speeds[x]), range(len(progresses))))
  return days

def solution(progresses, speeds):
  answer = []
  count = 1
  
  days = initDays(progresses, speeds)

  for i in range(len(days)):
    try:
      if days[i] < days[i+1]:
        answer.append(count)
        count = 1
      else:
        days[i+1] = days[i]
        count += 1
    except IndexError:
      answer.append(count)
  return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]	
print(solution(progresses, speeds))