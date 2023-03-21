# 프로그래머스 No.154540 무인도 여행
from collections import deque
from queue import PriorityQueue


def get_initialize_maps_to_number_maps(maps):
  number_maps = []
  for map in maps:
    map = map.replace("X", "0")
    map_list = [int(item) for item in list(map)]
    number_maps.append(map_list)
  return number_maps


def get_initialize_visited_list(n, m):
  return [[False] * m for _ in range(n)]


def bfs(start, visited, number_maps, n, m):
  x, y = start
  position_list = [start]
  queue = deque()
  queue.append((x, y))
  visited[x][y] = True

  dx = [-1, 0, 1, 0]
  dy = [0, -1, 0, 1]

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx >= 0 and nx < n and ny >= 0 and ny < m:
        if not visited[nx][ny] and number_maps[nx][ny] != 0:
          visited[nx][ny] = True
          position_list.append((nx, ny))
          queue.append((nx, ny))

  return position_list, visited


def is_livable(number_maps):
  food = 0
  for number_map in number_maps:
    food += sum(number_map)
  return False if food == 0 else True


def get_total_food(number_maps, position_list):
  food = 0
  for x, y in position_list:
    food += number_maps[x][y]
  return food


def solution(maps):
  answer = []
  priority_queue = PriorityQueue()
  number_maps = get_initialize_maps_to_number_maps(maps)
  n, m = len(number_maps), len(number_maps[0])
  visited = get_initialize_visited_list(n, m)

  if not is_livable(number_maps):
    return [-1]

  for x in range(n):
    for y in range(m):
      if not visited[x][y] and number_maps[x][y] != 0:
        position_list, visited = bfs((x, y), visited, number_maps, n, m)
        priority_queue.put(get_total_food(number_maps, position_list))
  while not priority_queue.empty():
    answer.append(priority_queue.get())
  return answer


maps = ["X591X", "X1X5X", "X231X", "1XXX1"]
print(solution(maps))
