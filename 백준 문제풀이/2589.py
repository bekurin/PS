from collections import deque

def initDistance():
  for i in range(n):
    for j in range(m):
      distance[i][j] = 0
      visited[i][j] = False


def bfs(x, y):
  queue = deque()
  queue.append((x,y))
  visited[x][y] = True
  count = 0
  dx = [-1, 0, 1, 0]
  dy = [0, -1, 0, 1]

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx >= 0 and nx < n and ny >= 0 and ny < m:
        if not visited[nx][ny] and data[nx][ny] == "L":
          distance[nx][ny] = distance[x][y] + 1
          count = max(count, distance[nx][ny])
          queue.append((nx, ny))
          visited[nx][ny] = True
  return count

n, m = map(int,input().split())

data = []
maxDistance = []
distance = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
for _ in range(n):
  data.append(list(str(input())))

for i in range(n):
  for j in range(m):
    if data[i][j] == "L":
      initDistance()
      maxDistance.append(bfs(i,j))

print(max(maxDistance))
