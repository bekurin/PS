from collections import deque

# DFS 알고리즘 함수
def dfs(v):
  print(v, end=' ')
  visited[v] = True
  for e in adj[v]:
    if not visited[e]:
      dfs(e)

# BFS 알고리즘 함수
def bfs(v):
  q = deque([v])
  while q:
    v = q.popleft()
    if not visited[v]:
      visited[v] = True
      print(v, end=' ')
      for e in adj[v]:
        if not visited[e]:
          q.append(e)

n,m,v = map(int, input().split())
adj = [[] for _ in range(n+1)]

# 2차원 배열에 각 노드에 연결된 다른 노드의 정보를 넣어준다.
for _ in range(m):
  x, y = map(int, input().split())
  adj[x].append(y)
  adj[y].append(x)

# 가장 작은 수 부터 접근하기 위해서 정렬을 시켜준다.
for e in adj:
  e.sort()

visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)
