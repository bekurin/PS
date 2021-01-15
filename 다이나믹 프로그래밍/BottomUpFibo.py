# 바텀업 방식 피보나치 수열
memo = [0] * 100

memo[1] = 1
memo[2] = 1
n = 99

for i in range(3, n+1):
  memo[i] = memo[i-1] + memo[i-2]

print(memo[n])