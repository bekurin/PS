# 백준 1010번 다리 놓기 (5c3)
t = int(input())

for _ in range(t):
  n, m = map(int,input().split())

  result = 1
  divide = 1

  if n > m:
    temp = n
    for i in range(m):
      result *= temp
      temp -= 1
    for j in range(m, 0, -1):
      divide *= j
    print(result // divide)
  else:
    temp = m
    for i in range(n):
      result *= temp
      temp -= 1
    for j in range(n, 0, -1):
      divide *= j
    print(result // divide)
