# 백준 No.5427 불
"""
answer의 최댓값을 2001로 초기화해서 문제를 풀어 25%에서 계속 "틀렸습니다"가 나왔습니다.
>> 1000 * 1000 그래프의 최단 이동 경로가 2000이다. 그리고 이거는 최대 이동 경로가 아니다.
"""
import sys
from collections import deque

input = sys.stdin.readline

def bfs(queue, visited):
  dx = [-1, 0, 1, 0]
  dy = [0, -1, 0, 1]

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < h and 0 <= ny < w:
        if visited[nx][ny] == 0 and maps[nx][ny] != '#':
          queue.append((nx, ny))
          visited[nx][ny] = visited[x][y] + 1 
  return visited

t = int(input())
for _ in range(t):
  maps = []
  w, h = map(int, input().split())
  for _ in range(h):
    maps.append(list(input().strip()))

  fire_visited, sang_visited = [[0] * w for _ in range(h)], [[0] * w for _ in range(h)]
  fire_queue, sang_queue = deque(), deque()

  for x in range(h):
    for y in range(w):
      if maps[x][y] == '@':
        sang_visited[x][y] = 1
        sang_queue.append((x, y))
      elif maps[x][y] == '*':
        fire_visited[x][y] = 1
        fire_queue.append((x, y))

  sang_visited = bfs(sang_queue, sang_visited)
  fire_visited = bfs(fire_queue, fire_visited)

  answer = float('inf')
  for x in range(h):
    for y in range(w):
      if sang_visited[x][y] > 0:
        if sang_visited[x][y] < fire_visited[x][y] or fire_visited[x][y] == 0:
          if x == 0 or y == 0 or x == (h-1) or y == (w-1):
            answer = min(answer, sang_visited[x][y])
  print(answer if answer != float('inf') else "IMPOSSIBLE")