# 프로그래머스 no.42839 소수 찾기
from itertools import permutations

def isPrime(number):

  if number in (0,1):
    return False

  for i in range(2, number // 2 + 1):
    if number % i == 0:
      return False
  return True

def solution(numbers):
  answer = 0
  items = set()
  data = list(map(int, numbers))
  
  for i in range(len(data)):
    for item in list(permutations(data, i + 1)):
      items.add(int("".join(map(str, item))))

  for item in items:
    if isPrime(item):
      answer += 1

  return answer


numbers = "011"
print(solution(numbers))

