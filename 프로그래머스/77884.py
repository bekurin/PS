# 프로그래머스 No.77884 약수의 개수와 덧셈
"""
1. 1의 약수는 1개이므로 count = 1로 초기화해준다.
2. 1의 제외한 수는 모두 1과 자기 자신을 약수로 가지므로 1과 자기 자신을 초기화해준 후에 2~number//2 범위를 순환하며 약수를 추가해준다.

best_solution
자기 자신에 루트를 씌운 값이 정수값이라면 해당 숫자는 i * i의 형태를 띈다는 것이므로 약수의 개수가 홀수가 된다.
"""
def get_alquit_by(number):
  alquit = [1, number]

  for i in range(2, number//2+1):
    if number % i == 0:
      alquit.append(i)
  return alquit

def solution(left, right):
  answer = 0
  for number in range(left, right+1):
    if number == 1: count = 1
    else: count  = len(get_alquit_by(number))

    answer += number if count % 2 == 0 else -number
  return answer

def best_solution(left, right):
  answer = 0
  for number in range(left, right+1):
    if int(number**0.5) == number**0.5:
      answer -= number
    else:
      answer += number
  return answer

left = 1
right = 18
print(solution(left, right))