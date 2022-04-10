# 백준 No.1629 곱셈
import sys
input = sys.stdin.readline

def solution(answer, n):
  if n == 1:
    return answer % c

  temp = solution(answer, n // 2)
  if n % 2 == 0:
    return (temp * temp) % c
  else:
    return (temp * temp * answer) % c

a, b, c = map(int, input().split())
print(solution(a, b))