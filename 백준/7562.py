# 백준 No.7562 나이트의 이동
"""
그래프 탐색
나이트의 이동 경로 8가지에 대해서 bfs 탐색을 실시해준다.
"""
import sys
from collections import deque

input = sys.stdin.readline

def bfs(n, current, target, visited):
  x, y = current
  queue = deque()
  queue.append((x, y, 0))
  visited[x][y] = True

  dx = [2, 1, -1, -2, -2, -1, 1, 2]
  dy = [-1, -2, -2, -1, 1, 2, 2, 1]

  while queue:
    x, y, move = queue.popleft()

    if x == target[0] and y == target[1]:
      return move

    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < n:
        if not visited[nx][ny]:
          visited[nx][ny] = True
          queue.append((nx, ny, move + 1))
  return -1

t = int(input())
info_list = []

for _ in range(t):
  temp = []
  for _ in range(3):
    temp.append(list(map(int, input().split())))
  info_list.append(temp)

t = 3
info_list = [[[8], [0, 0], [7, 0]], [[100], [0, 0], [30, 50]], [[10], [1, 1], [1, 1]]]

for info in info_list:
  n, current, target = info
  visited = [[False] * n[0] for _ in range(n[0])]
  print(bfs(n[0], current, target, visited))