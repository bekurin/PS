# 프로그래머스 No.68935 3진법 뒤집기
"""
1. n을 입력 받아 3진법으로 바꾼 수를 뒤집어서 반환해준다.
2. 파이썬의 int() 함수를 사용하여 10진법 결과를 반환한다.
"""
def get_reverse_notation_by(number, m):
  base = ''

  while number > 0:
    number, mode = divmod(number, m)
    base += str(mode)
  return base

def solution(n):
  base = get_reverse_notation_by(n, 3)
  return int(base, 3)

n = 45
print(solution(n))