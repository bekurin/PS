# 백준 No.15649 N과 M(1)

n, m = map(int, input().split())

answer = []
def dfs(n, m):

  if len(answer) == m:
    print(' '.join(map(str, answer)))
    return

  for i in range(1, n+1):
    if i not in answer:
      answer.append(i)
      dfs(n, m)
      answer.pop()
dfs(n, m)