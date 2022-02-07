# 백준 No.18809 Gaaaaaaaaaarden
"""
백트래킹, 조합, 순열, 너비 우선 탐색, 시뮬레이션
0 = 호수, 1 = 배양액을 뿌릴 수 없는 땅, 2 = 배양액을 뿌릴 수 있는 땅

1. 2를 1차원 배열에 저장하여 combination을 사용하여 경우의 수를 계산한다.
2. g + r의 개수만큼 1,2로 초록과 빨간 배양액의 자리 경우의 수를 계산한다.
3. 너비 우선 탐색을 진행하며 이동하는 곳이 다음 배양액과 만나는 지점이라면 maps를 -1로 초기화시켜 꽃이 피었다는 것을 알려주고, answer의 값을 1 추가해준다.
"""
import sys
import copy
from collections import deque
input = sys.stdin.readline

def bfs(queue, visited):
  answer = 0

  dx = [-1, 0, 1, 0]
  dy = [0, -1, 0, 1]

  while queue:
    x, y, second, media = queue.popleft()

    if copy_maps[x][y] == -1: 
      continue

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m:
        if visited[nx][ny][0] == 0 and copy_maps[nx][ny] != 0:
          visited[nx][ny] = [visited[x][y][0] + 1, media]
          queue.append((nx, ny, second + 1, media))
        elif visited[nx][ny][0] == second + 1:
          if visited[nx][ny][1] != media and copy_maps[nx][ny] != -1:
            answer += 1
            copy_maps[nx][ny] = -1
  return answer

def combination(index, numbers, length):
  global combination_list

  if len(numbers) == length:
    combination_list.append(numbers[:])
    return

  for i in range(index, len(enable_list)):
    numbers.append(enable_list[i])
    combination(i + 1, numbers, length)
    numbers.pop()

def permutation(g_index, r_index, numbers, length):
  global permutation_list

  if len(numbers) == length:
    permutation_list.append(numbers[:])    
    return

  for i in range(g_index, len(g_list)):
    numbers.append(g_list[i])
    permutation(i + 1, r_index, numbers, length)
    numbers.pop()

  for i in range(r_index, len(r_list)):
    numbers.append(r_list[i])
    permutation(g_index, i + 1, numbers, length)
    numbers.pop()

answer = 0
n, m, g, r = map(int, input().split())

maps = []
for _ in range(n):
  maps.append(list(map(int, input().split())))

copy_maps = []
enable_list = []
for x in range(n):
  for y in range(m):
    if maps[x][y] == 2:
      enable_list.append(m * x + y)

combination_list = [] # 비료를 넣을 수 있는 자리 조합
combination(0, [], g + r)

permutation_list = [] # 비료의 자리
g_list = [1] * g
r_list = [2] * r
permutation(0, 0, [], g + r)

for combination in combination_list:
  for permutation in permutation_list:
    queue = deque()
    copy_maps = copy.deepcopy(maps)
    visited = [[[0,0]] * m for _ in range(n)]
    for item in zip(combination, permutation):
      x, y = item[0] // m, item[0] % m
      queue.append((x, y, 1, item[-1]))
      visited[x][y] = [1, item[-1]]
    answer = max(answer, bfs(queue, visited))
print(answer)
