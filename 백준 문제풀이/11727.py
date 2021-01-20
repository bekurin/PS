# 백준 11727번 2n타일링-2
# 다이나믹 프로그래밍 바텀업 방식 런타임 에러 발생, 탑다운 방식으로 해결
n = int(input())

dp = [0 for _ in range(n+1)]

def tiling(x):
  if x < 3:
    if x == 1: return 1
    else: return 3
  if dp[x] != 0:
    return dp[x]
  dp[x] = tiling(x-1) + tiling(x-2) * 2
  return dp[x]
print(tiling(n) % 10007)