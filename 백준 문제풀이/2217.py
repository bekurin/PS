# 백준 2217번 로프 (최댓값)
n = int(input())

ropeWeight = []
for _ in range(n):
  ropeWeight.append(int(input()))

ropeWeight = sorted(ropeWeight, reverse=False)

maxWeight = 0
for i in range(n, 0, -1):
  maxWeight = max(maxWeight, ropeWeight[n-i] * i)

print(maxWeight)