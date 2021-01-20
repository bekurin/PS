# 백준 9095번 1,2,3 더하기(다이나믹 프로그래밍)
t = int(input())

answer = []
for _ in range(t):
  answer.append(int(input()))

dp = [1,2,4]

for i in range(3, max(answer)):
  dp.append(dp[i-1] + dp[i-2] + dp[i-3])

for i in answer:
  print(dp[i-1])