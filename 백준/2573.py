# 백준 No.2573 빙산
"""
그래프 탐색
깊은 복사, 바다와 인접한 면의 빙하 녹이기
"""
import sys
from collections import deque

input = sys.stdin.readline

def bfs(target, visited, maps):
  x, y = target
  queue = deque()
  queue.append((x, y))
  visited[x][y] = True
  maps_copy = [item[:] for item in maps]

  dx = [-1, 0, 1, 0]
  dy = [0, -1, 0, 1]

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m:
        if maps[nx][ny] == 0 and maps_copy[x][y] > 0:
          maps_copy[x][y] -= 1
        if visited[nx][ny] == 0 and maps[nx][ny] > 0:
          queue.append((nx, ny))
          visited[nx][ny] = True
  return maps_copy

# n, m = map(int, input().split())
# maps = []

# for _ in range(n):
#   maps.append(list(map(int, input().split())))

maps = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 10, 10, 10, 0, 0, 0],
  [0, 10, 0, 10, 0, 0, 0], 
  [0, 10, 10, 10, 0, 0, 0], 
  [0, 0, 0, 0, 0, 0, 0]
]
n, m = len(maps), len(maps[0])

answer, count = 0, 0
while count < 2:
  count = 0
  answer += 1
  visited = [[False] * m for _ in range(n)]

  for x in range(n):
    for y in range(m):
      if maps[x][y] > 0 and not visited[x][y]:
        count += 1
        maps = bfs([x, y], visited, maps)
  
  if count == 0:
    answer = 1
    break
print(answer - 1)