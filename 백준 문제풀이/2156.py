# 백준 2156번 포도주 시식(다이나믹 프로그래밍)
n = int(input())
weight = [0]

for _ in range(n):
  weight.append(int(input()))
dp = [0]
dp.append(weight[1])

if n > 1:
  dp.append(weight[1] + weight[2])
for i in range(3, n+1):
  dp.append(max(dp[i-1], dp[i-3] + weight[i-1] + weight[i], dp[i-2] + weight[i]))
print(dp[n])