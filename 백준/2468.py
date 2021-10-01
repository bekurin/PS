# 백준 No.2468 안전 영역
from collections import deque

def setMaps(instability):
  for i in range(n):
    for j in range(n):
      visited[i][j] = False
      if maps[i][j] <= instability:
        maps[i][j] = -1;

def dfs(x, y):
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

      if nx >= 0 and nx < n and ny >= 0 and ny < n:
        if not visited[nx][ny] and maps[nx][ny] != -1:
          visited[nx][ny] = True
          queue.append((nx, ny))

n = int(input())

maps = []
max_maps = 0
visited = [[False] * n for _ in range(n)]
answer = []

for i in range(n):
  maps.append(list(map(int, input().split(" "))))
  if max_maps < max(maps[i]):
    max_maps = max(maps[i])

for i in range(max_maps):
  setMaps(i)
  count = 0
  for i in range(n):
    for j in range(n):
      if maps[i][j] != -1 and not visited[i][j]:
        count += 1
        dfs(i, j)
  answer.append(count)

print(max(answer))
