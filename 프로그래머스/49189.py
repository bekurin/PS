# 프로그래머스 No.49189 가장 먼 노드
from collections import deque

def bfs(graph, start, visited, distance):
  queue = deque([start])
  visited[start] = True

  while queue:
    v = queue.popleft()

    for i in graph[v]:
      if not visited[i]:
        distance[i] = distance[v] + 1 
        queue.append(i)
        visited[i] = True

def edge_to_graph(n, edge):
  graph = [[] for _ in range(n + 1)]

  for v1, v2 in edge:
    graph[v1].append(v2)
    graph[v2].append(v1)
  return graph

def solution(n, edge):
  graph = edge_to_graph(n, edge)
  visited = [False] * (n + 1)
  distance = [1] * (n + 1)

  bfs(graph, 1, visited, distance)
  return distance.count(max(distance))
