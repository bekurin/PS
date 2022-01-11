# 프로그래머스 No.67257  수식 최대화
"""
tech: stack, permutation
1. 순열을 사용하여 ("*", "-", "+")의 모든 경우의 수를 만들어준다.
2. 임의의 경우의 수를 선택한다.
3. 주어진 식을 숫자와 수식으로 나누어 data에 저장해준다.
4. 높은 우선순위의 수식을 선택한다.
5. data에서 값을 하나씩 가져와 current에 저장하고, 4의 결과와 비교한다.
6. 5의 결과가 참이라면 stack의 마지막 값과 data의 첫번째 값을 current에 맞게 계산하여 stack에 저장한다.
7. 5의 결과가 거짓이라면 stack에 temp를 저장한다.
8. stack의 값을 data에 저장한다.
9. 4를 반복한다.
10. 9가 끝난 결과의 최댓값을 answer에 저장한다.
11. 2를 반복한다.
 """
from itertools import permutations

def get_data_by(expression):
  data = []
  temp = ""
  for s in expression:
    if s.isdigit():
      temp += s
    else:
      data.append(temp)
      data.append(s)
      temp = ""

  data.append(temp)
  return data

def calculate_by_priorities(data, priorities):
  for priority in priorities:
    stack = []
    while data:
      current = data.pop(0)
      if current == priority:
        stack.append(calculate_by(current, stack.pop(), data.pop(0)))
      else:
        stack.append(current)
    data = stack
  return abs(data[0])

def calculate_by(formula, num1, num2):
  num1, num2 = int(num1), int(num2)
  if formula == '-':
    return num1 - num2
  elif formula == '+':
    return num1 + num2
  else:
    return num1 * num2

def solution(expression):
  answer = 0
  priorities = list(permutations(("*", "+", "-"), 3))

  for priority in priorities:
    data = get_data_by(expression)
    answer = max(answer, calculate_by_priorities(data ,priority))
  return answer

expression = "100-200*300-500+20"
print(solution(expression))