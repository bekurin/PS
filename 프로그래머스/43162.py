# 프로그래머스 No.43162 네트워크
from collections import deque

def bfs(graph, start, n, visited):
  queue = deque([start])
  visited[start] = True
  
  while queue:
    v = queue.popleft()

    for i in range(len(graph[v])):
      if graph[v][i] == 1 and not visited[i]:
        queue.append(i)
        visited[i] = True

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
      if not visited[i]:
        answer += 1
        bfs(computers, i, n, visited)
    return answer

coputers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
n = 3
print(solution(n, coputers))