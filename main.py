t = int(input())
m, n, k = map(int, input().split())
adj = [[0] * m for _ in range(n)]

# 2차원 배열에 각 노드에 연결된 다른 노드의 정보를 넣어준다.
for _ in range(k):
  y, x = map(int, input().split())
  adj[x][y] = 1

def dfs(x, y):
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  if adj[x][y] == 1:
    adj[x][y] == 0
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  return False

result = 0
for i in range(m):
  for j in range(n):
    if dfs(i, j) == True:
      result += 1
print(result)