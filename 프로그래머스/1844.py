# 프로그래머스 No.1844 게임 맵 최단거리
"""
게임 맵을 bfs 알고리즘을 사용하여 탐색을 진행한다. 탐색 과정에서 상대 팀 진영을 만나게 된다면 그때까지의 distance를 반환해준다. 탐색이 종료되는 동안 distance를 반환하지 않았으면 상대 팀 진영에 도착할 수 있는 방법이 없다는 것이므로 -1을 반환해준다.
"""
from collections import deque

def bfs(n,m,maps,visited):
  queue = deque()
  queue.append((0,0,1))
  visited[0][0] = True

  dx = [-1, 0, 1, 0]
  dy = [0, -1, 0, 1]

  while queue:
    x, y, distance = queue.popleft()

    if x == (n-1) and y == (m-1):
      return distance

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m:
        if not visited[nx][ny] and maps[nx][ny] == 1:
          visited[nx][ny] = True
          queue.append((nx, ny, distance + 1))
  return -1

def solution(maps):
  n, m = len(maps), len(maps[0])
  visited = [[False] * m for _ in range(n)]
  return bfs(n,m,maps,visited)

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))