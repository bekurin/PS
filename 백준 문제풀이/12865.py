# 백준 12865번 평범한 배낭
# 절대 평범하지 않음
n, k = map(int, input().split())
weight = [0]
value = [0]

for _ in range(n):
  w, v = map(int, input().split())
  weight.append(w)
  value.append(v)

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for w in range(1, n+1):
  for i in range(1, k+1):
    if i >= weight[w]:
      dp[w][i] = max(dp[w-1][i], dp[w-1][i-weight[w]] + value[w])
    else:
      dp[w][i] = dp[w-1][i]
      
print(dp[n][k])

