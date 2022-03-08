# 백준 No.15686 치킨 배달

import copy
from collections import deque

def bfs(x, y):
  distance = 0
  queue = deque()
  visited = [[False] * n for _ in range(n)]

  visited[x][y] = True
  queue.append((x, y, 1))

  dx = [-1, 0, 1, 0]
  dy = [0, -1, 0, 1]

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < n:
        if not visited[nx][ny]:
          pass

def combination(index, numbers):

  if len(numbers) == m:
    test_list.append(numbers[:])
    return

  for i in range(index, len(chicken_list)):
    numbers.append(chicken_list[i])
    combination(i + 1, numbers)
    numbers.pop()

# n, m = map(int, input().split())
# visited = [[False] * n for _ in range(n)]

# maps = []
# for _ in range(n):
#   maps.append(list(map(int, input().split())))

n, m = 5, 3
maps = [
  [0, 0, 1, 2, 2], 
  [0, 0, 2, 2, 1], 
  [0, 1, 2, 0, 0],
  [0, 0, 1, 0, 0], 
  [0, 0, 0, 0, 2]
]

chicken_list, test_list = [], []
for x in range(n):
  for y in range(n):
    if maps[x][y] == 2:
      maps[x][y] = 0
      chicken_list.append(x * n + y % n)

combination(0, [])

for test in test_list:
  temp_maps = copy.deepcopy(maps)
  for position in test:
    x = position // n
    y = position % n

    temp_maps[x][y] = 2
  print(temp_maps)
  
