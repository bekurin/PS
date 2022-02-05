# 백준 No.1941 소문난 칠공주
import sys
from collections import deque

input = sys.stdin.readline

def combination(index, number_list, numbers, doyeon):
  if doyeon >= 4:
    return

  if len(numbers) == 7:
    answer_list.append(numbers[:])
    return

  for i in range(index, len(number_list)):
    x, y = number_list[i] // 5, number_list[i] % 5
    
    numbers.append(number_list[i])
    if maps[x][y] == 'Y':
      combination(i + 1, number_list, numbers, doyeon + 1)
    else:
      combination(i + 1, number_list, numbers, doyeon)
    numbers.pop()  

def bfs(target, boards, visited):
  global depth
  x, y = target
  queue = deque()
  queue.append((x, y))
  visited[x][y] = True

  dx = [-1, 0, 1, 0]
  dy = [0, -1, 0, 1]

  while queue:
    x, y = queue.popleft()
    if depth == 7: return True

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < 5 and 0 <= ny < 5:
        if not visited[nx][ny] and boards[nx][ny] == 1:
          depth += 1
          visited[nx][ny] = True
          queue.append((nx, ny))
  return False

answer_list, maps = [], []
# for _ in range(5):
#   maps.append(list(input().strip()))

maps = [['S', 'S', 'S', 'S', 'S'], ['S', 'S', 'S', 'S', 'S'], ['S', 'S', 'S', 'S', 'S'], ['S', 'S', 'S', 'S', 'S'], ['S', 'S', 'S', 'S', 'S']]

count, depth = 0, 1
combination(0, list(range(25)), [], 0)

for answer in answer_list:
  x, y, depth = 0, 0, 1
  boards = [[0] * 5 for _ in range(5)]

  for item in answer:
    x, y = item // 5, item % 5
    boards[x][y] = 1

  visited = [[False] * 5 for _ in range(5)]
  if bfs([x, y], boards, visited):
    count += 1

print(count)