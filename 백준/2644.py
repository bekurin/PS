# 백준 No.2644 촌수계산
"""
그래프 탐색
visited를 0으로 초기화한 후에 탐색 깊이에 따라 값을 대입해주는 방식
한번의 탐색으로 모든 촌수를 계산하기 때문에 visited[target]의 값이 0이라면 -1을 반환하고, visited[target]의 값이 0보다 크다면 그 값을 반환해준다.
"""
import sys
from collections import deque
input = sys.stdin.readline


def bfs(v, graph, visited):
  queue = deque()
  queue.append(v)

  while queue:
    v = queue.popleft()
    for n in graph[v]:
      if visited[n] == 0:
        visited[n] = visited[v] + 1
        queue.append(n)

def dfs(v, graph, visited):
  for n in graph[v]:
    if visited[n] == 0:
      visited[n] = visited[v] + 1
      dfs(n, graph, visited)

def convert_data_to_adjacent_list(data, n):
  adjacent_list = [[] for _ in range(n + 1)]
  for vertex, edge in data:
    adjacent_list[vertex].append(edge)
    adjacent_list[edge].append(vertex)
  return adjacent_list

def bfs_solution(data,n,start,target):
  visited = [0] * (n+1)
  graph = convert_data_to_adjacent_list(data,n)
  bfs(start, graph, visited)
  return visited[target] if visited[target] > 0 else -1

def dfs_solution(data, n, start, target):
  visited = [0] * (n+1)
  graph = convert_data_to_adjacent_list(data, n)
  dfs(start, graph, visited)
  return visited[target] if visited[target] > 0 else -1

# n = int(input())
# start, target = map(int, input().split())
# m = int(input())
# data = []

# for _ in range(m):
#   data.append(list(map(int, input().split())))
# print(bfs_solution(data, n, start, target))

n = 9
start, target = 7, 3
m, answer = 7, -1
data = [[1, 2], [1, 3], [2, 7], [2, 8], [2, 9], [4, 5], [4, 6]]
print(bfs_solution(data,n,start,target))
print(dfs_solution(data,n,start,target))