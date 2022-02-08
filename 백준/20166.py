# 백준 No.20166 문자열 지옥에 빠진 호석
import sys
from collections import deque
input = sys.stdin.readline

def bfs(queue):

  dx = [-1, 0, 1, 0, 1, 1, -1, -1]
  dy = [0, -1, 0, 1, -1, 1, 1, -1]

  while queue:
    x, y, word, distance = queue.popleft()

    if distance >= 5: continue

    if word in quiz_dict:
      quiz_dict[word] += 1

    for i in range(8):
      nx = (x + dx[i] + n) % n
      ny = (y + dy[i] + m) % m

      if 0 <= nx < n and 0 <= ny < m:
        queue.append((nx, ny, word + maps[nx][ny], distance + 1))
  return 0
        
n, m, k = map(int, input().split())
maps, quiz_dict = [], {}

for _ in range(n):
  maps.append(input().strip())

for _ in range(k):
  quiz_dict[input().strip()] = 0

queue = deque()
for x in range(n):
  for y in range(m):
    queue.append((x, y, maps[x][y], 1))
bfs(queue)

for key, value in quiz_dict.items():
  print(value)