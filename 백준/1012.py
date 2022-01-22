# 백준 No.1012 유기농 배추
from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x,y))
  visited[x][y] = True

  dx = [-1, 0, 1, 0]
  dy = [0, -1, 0, 1]

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx >= 0 and nx < m and ny >= 0 and ny < n:
        if not visited[nx][ny] and maps[nx][ny] == 1:
          visited[nx][ny] = True
          queue.append((nx,ny))

t = int(input())

for _ in range(t):
  n, m, k = map(int, input().split())
  maps = [[0] * n for _ in range(m)]
  visited = [[False] * n for _ in range(m)]
  count = 0

  for _ in range(k):
    y, x = map(int,input().split())
    maps[x][y] = 1

  for x in range(m):
    for y in range(n):
      if not visited[x][y] and maps[x][y] == 1:
        bfs(x, y)
        count += 1
  print(count)

  