# 백준 No.7569 토마토
from collections import deque

def bfs():
  dx = [-1, 0, 1, 0, 0, 0]
  dy = [0, -1, 0, 1, 0, 0]
  dz = [0, 0, 0, 0, -1, 1]

  while queue:
    x, y, z = queue.popleft()

    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]

      if nx < n and nx >= 0 and ny < m and ny >= 0 and nz < h and nz >= 0:
        if not visited[nz][ny][nx] and data[nz][ny][nx] == 0:
          queue.append((nx,ny,nz))
          data[nz][ny][nx] = data[z][y][x] + 1
          visited[nz][ny][nx] = True

n, m, h = map(int, input().split(' '))
data = []
queue = deque()
answer, count = 0, 0
isExist0 = True

for _ in range(h):
  temp = []
  for _ in range(m):
    line = list(map(int, input().split(' ')))
    temp.append(line)
  data.append(temp)

visited = []
for _ in range(h):
  visited.append([[False] * n for _ in range(m)])


for z in range(h):
  for y in range(m):
    for x in range(n):
      if data[z][y][x] == 1:
        visited[z][y][x] = True
        queue.append((x, y, z))
bfs()

for z in range(h):
  for y in range(m):
    for x in range(n):
      if data[z][y][x] == 0:
        isExist0 = False
      answer = max(answer, data[z][y][x])

if isExist0:
  print(answer-1)
else:
  print(-1)