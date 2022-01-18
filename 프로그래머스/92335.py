# 프로그래머스 No.92335 k진수에서 소수 개수 구하기
def convert_by(n, mode):
  base = ''
  while n > 0:
    n, mod = divmod(n, mode)
    base += str(mod)
  return base[::-1]

def is_prime(n):
  if n < 2: return False

  for i in range(2, n // 2 + 1):
    if n % i == 0:
      return False
  return True

def solution(n,k):
  answer = 0
  number_list = [int(item) for item in convert_by(n, k).split('0') if item != ""]

  print(number_list)
  for number in number_list:
    if is_prime(number):
      answer += 1

  return answer

n = 437674
k = 3
print(solution(n, k))