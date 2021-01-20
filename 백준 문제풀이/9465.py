# 백준 9465번 스티커 (다이나믹 프로그래밍)
t = int(input())
for i in range(t):
  n = int(input())
  value = []
  for j in range(2):
    value.append(list(map(int, input().split())))

  value[0][1] += value[1][0]
  value[1][1] += value[0][0]
  for k in range(2, n):
    value[0][k] += max(value[1][k-1], value[1][k-2])
    value[1][k] += max(value[0][k-1], value[0][k-2])
  print(max(value[0][n-1], value[1][n-1]))