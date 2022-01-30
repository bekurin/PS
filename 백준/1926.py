# 백준 No.1926 그림
"""
maps를 순환하며 아직 방문하지 않은 그림에 대해서 bfs, dfs를 수행한 후에 area를 answer 배열에 추가해준다.
- 그림의 개수: len(answer)
- 가장 큰 그림: max(answer)
"""
import sys
from collections import deque

input = sys.stdin.readline

def bfs(x,y,visited,maps):
  queue = deque()
  queue.append((x,y))
  visited[x][y] = True
  n, m = len(maps), len(maps[0])

  dx = [-1, 0, 1, 0]
  dy = [0, -1, 0, 1]

  area = 1
  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if not visited[nx][ny] and maps[nx][ny] == 1:
          queue.append((nx, ny))
          visited[nx][ny] = True
          area += 1
  return area

def dfs(x,y,visited,maps,area):
  visited[x][y] = True
  n, m = len(maps), len(maps[0])

  dx = [-1, 0, 1, 0]
  dy = [0, -1, 0, 1]

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < m:
      if not visited[nx][ny] and maps[nx][ny] == 1:
        visited[nx][ny] = True
        area = dfs(nx,ny,visited,maps,area+1)
  return area
    
def solution(maps, n, m):
  answer = []
  visited = [[False] * m for _ in range(n)]

  for x in range(n):
    for y in range(m):
      if maps[x][y] == 1 and not visited[x][y]:
        answer.append(bfs(x,y,visited,maps))
  return answer

# n, m = map(int, input().split())
# maps = []

# for _ in range(n):
#   maps.append(list(map(int, input().split())))

n, m = 6, 5
maps = [[1, 1, 0, 1, 1], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0], [1, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]]

answer = solution(maps, n, m)

print(len(answer))
print(max(answer)) if answer else print(0) 