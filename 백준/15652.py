# 백준 No.15652 N과 M(4)
"""
백트래킹, 깊이 우선 탐색
"""
def dfs(index, number_list, numbers):
  if len(numbers) == m:
    for number in numbers:
      print(number, end = " ")
    print("")
    return
  
  for i in range(index, len(number_list)):
    numbers.append(number_list[i])
    dfs(i, number_list, numbers)
    numbers.pop()

n, m = map(int, input().split())
dfs(0, list(range(1,n+1)), [])