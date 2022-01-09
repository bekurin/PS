# 백준 No.4963 섬의 개수
"""
category: 너비 우선 탐색, 그래프 탐색

해결 순서
1. n, m을 입력 받는다.
2. 둘의 값이 0이 아나리면 반복문을 돌면서 땅을 찾는다.
3. 아직 방문하지 않은 땅이라면 섬의 개수를 1 증가시킨다.
4. 방문 처리 후 bfs 알고리즘을 실행시킨다.
5. 1을 반복한다.
"""

from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x,y))
  visited[x][y] = True

  dx = [-1, 0, 1, 0, 1, 1, -1, -1]
  dy = [0, -1, 0, 1, -1, 1, 1, -1]

  while queue:
    x, y = queue.popleft()
    
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < m and 0 <= ny < n:
        if not visited[nx][ny] and data[nx][ny] == 1: 
          queue.append((nx, ny))
          visited[nx][ny] = True

def solution(n, m):
  answer = 0
  for i in range(m):
    for j in range(n):
      if data[i][j] == 1 and visited[i][j] == False: 
        bfs(i, j)
        answer += 1
  return answer

while True:
  n, m = map(int, input().split())
  visited = [[False] * n for _ in range(m)]
  data = []

  if n == 0 and m == 0:
    break
    
  for _ in range(m):
    data.append(list(map(int, input().split())))

  print(solution(n, m))