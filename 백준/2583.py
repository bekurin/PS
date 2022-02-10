# 백준 No.2583 영역 구하기
"""
그래프 이론, 그래프 탐색, 너비 우선 탐색
"""
import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y, visited):
  queue = deque()
  queue.append((x, y))
  visited[x][y] = True

  area = 1
  dx = [-1, 0, 1, 0]
  dy = [0, -1, 0, 1]

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m:
        if not visited[nx][ny] and maps[nx][ny] == 0:
          area += 1
          queue.append((nx, ny))
          visited[nx][ny] = True
  return area

m, n, k = map(int, input().split())
rectangle_list = []
for _ in range(k):
  rectangle_list.append(list(map(int, input().split())))

maps = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for x1, y1, x2, y2 in rectangle_list:
  for x in range(x1, x2):
    for y in range(y1, y2):
      maps[x][y] = 1

count = 0
area_list = []
for x in range(n):
  for y in range(m):
    if maps[x][y] == 0 and not visited[x][y]:
      count += 1
      area_list.append(bfs(x, y, visited))

print(count)
for area in sorted(area_list):
  print(area, end = " ")