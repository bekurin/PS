# 백준 2606번 바이러스 문제(DFS)
n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0

# ★★★
# 2차원 배열에 각 노드에 연결된 다른 노드의 정보를 넣어준다. 
for _ in range(m):
  x, y = map(int, input().split())
  adj[x].append(y)
  adj[y].append(x)

def dfs(array, v, visited):
  global count
  count += 1
  visited[v] = True
  for i in array[v]:
    if not visited[i]:
      count = dfs(array,i,visited)
  return count

print(dfs(adj, 1, visited) - 1)