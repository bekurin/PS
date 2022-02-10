# 백준 No.6593 상범 빌딩
"""
그래프 이론, 그래프 탐색, 너비 우선 탐색
"""
import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y, z, visited):
  global answer
  queue = deque()
  queue.append((x, y, z, 0))
  visited[z][x][y] = True

  dx = [-1, 0, 1, 0, 0, 0]
  dy = [0, -1, 0, 1, 0, 0]
  dz = [0, 0, 0, 0, -1, 1]

  while queue:
    x, y, z, time = queue.popleft()

    if total_maps[z][x][y] == 'E':
      answer = time
      return True

    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]

      if 0 <= nx < R and 0 <= ny < C and 0 <= nz < L:
        if not visited[nz][nx][ny] and total_maps[nz][nx][ny] != '#':
          queue.append((nx, ny, nz, time + 1))
          visited[nz][nx][ny] = True
  return False

answer = 0

while True:
  answer = 0
  L, R, C = map(int, input().split())
  if [L, R, C] == [0, 0, 0]:
    break

  total_maps = []
  visited = [[[False] * C for _ in range(R)] for _ in range(L)]
  for _ in range(L):
    maps = []
    for _ in range(R):
      maps.append(input().strip())
    total_maps.append(maps)
    input()

  for z in range(L):
    for x in range(R):
      for y in range(C):
        if total_maps[z][x][y] == 'S':
          if bfs(x, y, z, visited):
            print("Escaped in " + str(answer) + " minute(s).")
          else:
            print("Trapped!")