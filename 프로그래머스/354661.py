# 프로그래머스 No.354661 스킬 3 문제 1
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
  answer = 0
  graph = edge_to_graph(n, edge)
  visited = [False] * (n + 1)
  distance = [1] * (n + 1)
  
  bfs(graph, 1, visited, distance)

  for item in distance:
    if item == max(distance):
      answer += 1
  return answer

n = 6
edge =[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))