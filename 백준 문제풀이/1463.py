# 백준 1464번 1로 만들기
x = int(input())

dp = [0 for _ in range(x+1)]

for i in range(2, x+1):
  dp[i] = dp[i-1] + 1

  if i%2==0 and dp[i] > dp[i//2] + 1:
    dp[i] = dp[i//2] + 1
  if i%3==0 and dp[i] > dp[i//3] + 1:
    dp[i] = dp[i//3] + 1
print(dp[x])