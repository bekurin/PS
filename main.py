# 백준 No.16236 아기 상어
import sys
from collections import deque

input = sys.stdin.readline

def bfs(x,y,shark, target, visited):
  queue = deque()
  queue.append((x,y,shark))
  visited[x][y] = True

  dx = [-1, 0, 1, 0]
  dy = [0, -1, 0, 1]

  while queue:
    x, y, shark = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

def solution(spaces, n):
  answer = 0
  shark = 2
  visited = [[False] * n for _ in range(n)]

  for x in range(n):
    for y in range(n):
      if spaces[x][y] != 0 and shark > spaces[x][y]:
        shark = bfs(x,y,shark, spaces[x][y], visited)

