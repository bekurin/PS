# 프로그래머스 No.43162 네트워크
"""
1. start를 큐에 넣어주고, 해당 노드를 방문 처리 해준다.
2. 큐에서 노드의 값을 꺼내준다.
3. 2의 결과 노드의 인접행렬 값을 확인하여 값이 1이고, 아직 방문하지 않은 노드의 값이 있는지 확인한다.
4. 3의 결과 노드를 큐에 넣어주고, 방문 처리를 해준다.
5. 큐가 빌 때까지 2의 과정을 반복한다.
"""

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