# 프로그래머스 no.42862 체육복
def initArray(lost, reserve, n):
    student = [True] * n
    
    new_lost = list(set(lost) - set(reserve))
    new_reserve = list(set(reserve) - set(lost))

    for item in new_lost:
        student[item-1] = False

    return student, new_reserve

def solution(n, lost, reserve):
  items = []
  student, reserve = initArray(lost, reserve, n)

  for item in reserve:
    items.append(item-2)
    items.append(item)

    for item in items:
      if item >= 0 and item < n:
        if not student[item]:
          student[item] = True
          break
                    
  return student.count(True)

n = 5
lost = [2,3,5]
reserve = [1,5]

print(solution(n, lost, reserve))