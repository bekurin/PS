# 프로그래머스 No.12945 피보나치 수
def solution(n):
  fibo = [0,1,1]

  if n == 1 or n == 2:
    return fibo[n]
  
  for i in range(3, n+1):
    fibo.append(fibo[i-1] + fibo[i-2])
  return fibo[n] % 1234567

n = 5
print(solution(n))  