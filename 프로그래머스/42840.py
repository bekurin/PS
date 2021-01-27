# 프로그래머스 42840 모의고사 문제 (완전탐색))
def solution(answer):
  student1 = [1,2,3,4,5]            # 5개
  student2 = [2,1,2,3,2,4,2,5]      # 8개
  student3 = [3,3,1,1,2,2,4,4,5,5]  # 10개

  getRightStudent1 = 0
  getRightStudent2 = 0
  getRightStudent3 = 0

  data = []
  for i in range(len(answer)):
    if answer[i] == student1[i%5]:
      getRightStudent1 += 1
    if answer[i] == student2[i%8]:
      getRightStudent2 += 1
    if answer[i] == student3[i%10]:
      getRightStudent3 += 1

  data.append((1, getRightStudent1))
  data.append((2, getRightStudent2))
  data.append((3, getRightStudent3))

  data = sorted(data, key=lambda x: -x[1])
  answer = []

  if data[0][1] == data[1][1]:
    if data[1][1] == data[2][1]:
      answer.append(data[0][0])
      answer.append(data[1][0])
      answer.append(data[2][0])
    else:
      answer.append(data[0][0])
      answer.append(data[1][0])
  else:
    answer.append(data[0][0])
  return answer
