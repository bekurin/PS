# 백준 2667번 단지번호붙이기 (dfs)
def dfs(x, y):
  dx = [-1, 0, 1, 0] # 아래 왼쪽 위 오른쪽
  dy = [0, -1, 0, 1] # 아래 왼쪽 위 오른쪽

  visited[x][y] = True

  if data[x][y] == 1:
    answer[count] += 1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx >= 0 and nx < n and ny >= 0 and ny < n:
        if not visited[nx][ny]:
          dfs(nx, ny)

n = int(input())
data = []
answer = []
visited = [[False] * n for _ in range(n)]
count = 0

for _ in range(n):
  data.append(list(map(int,str(input()))))

for i in range(n):
  for j in range(n):
    if data[i][j] == 1 and not visited[i][j]:
      answer.append(0)
      dfs(i, j)
      count += 1

print(len(answer))
answer.sort()
for i in answer:
  print(i)