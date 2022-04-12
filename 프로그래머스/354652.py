# 프로그래머스 No.354652 문제 1
from collections import deque  

def solution(maps):
  x, y = 0, 0
  m, n = len(maps), len(maps[0])
  visited = [[False] * n for _ in range(m)]
  
  queue = deque()
  queue.append((x, y))
  visited[x][y] = True

  dx = [-1, 0, 1, 0]
  dy = [0, -1, 0, 1]

  while queue:
    x, y = queue.popleft()

    if x == (m-1) and y == (n-1): return maps[-1][-1]
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < m and 0 <= ny < n:
        if not visited[nx][ny] and maps[nx][ny] == 1:
          visited[nx][ny] = True
          maps[nx][ny] = maps[x][y] + 1
          queue.append((nx, ny))
  return -1