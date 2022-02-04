# 백준 No.15651 N과 M(3)
"""
백트래킹, 깊이 우선 탐색
중복된 수를 뽑아도 되기 때문에 dfs 재귀 함수를 호출 할 때에 number_list의 첫번째부터 탐색을 해준다.
"""
def dfs(number_list, numbers):
  if len(numbers) == m:
    for number in numbers:
      print(number, end = " ")
    print("")
    return
  
  for i in range(0, len(number_list)):
    numbers.append(number_list[i])
    dfs(number_list, numbers)
    numbers.pop()

n, m = map(int, input().split())
dfs(list(range(1,n+1)), [])
