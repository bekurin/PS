# 백준 No.15654 N과 M (5)
"""
백트래킹, 깊이 우선 탐색
numbers에 저장되었던 값들이 중복으로 저장되면 안되기 때문에 index에 이전에 저장되었던 값들의 인덱스를 저장하여 중북으로 저장되지 않게 처리
"""
def dfs(index, numbers):
  if len(numbers) == m:
    for number in numbers:
      print(number, end = " ")
    print("")
    return
  
  for i in range(0, len(number_list)):
    if i not in index:
      numbers.append(number_list[i])
      index.append(i)
      dfs(index, numbers)
      index.pop()
      numbers.pop()

# n, m = map(int, input().split())
# number_list = sorted(list(map(int, input().split())))
# dfs(0, [])

n, m = 4, 4
number_list = [1231, 1232, 1233, 1234]
dfs([], [])