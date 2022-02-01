# 백준 No.5014 스타트링크
"""
2가지 방향 탐색에 대한 그래프 탐색 문제입니다.
"""
import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, visited):
  queue = deque()
  visited[start] = True
  queue.append((start, 0))
  
  dx = [U, -D]

  while queue:
    x, count = queue.popleft()

    if x == G:
      return count

    for i in range(2):
      nx = x + dx[i]

      if 0 < nx <= F:
        if not visited[nx]:
          queue.append((nx, count + 1))
          visited[nx] = True
  return -1
  
F, S, G, U, D = map(int,input().split())
visited = [False] * (F + 1)
answer = bfs(S, visited)
print(answer if answer != -1 else "use the stairs")