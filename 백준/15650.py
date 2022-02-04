# 백준 No.15650 N과 M(2)
"""
백트래킹, 깊이 우선 탐색
dfs(index + 1, number_list, numbers) 다음과 같이 index를 넘기게 되면 중복된 값을 선택할 수 있다. 따라서 dfs(i + 1, number_list, numbers) 과 같이 현재 append된 number_list의 index + 1값을 넘겨준다.
"""
def dfs(index, number_list, numbers):
  
  if len(numbers) == m:
    for number in numbers:
      print(number, end = " ")
    print("")
    return
  
  for i in range(index, len(number_list)):
    numbers.append(number_list[i])
    dfs(i + 1, number_list, numbers)
    numbers.pop()

n, m = map(int, input().split())
dfs(0, list(range(1,n+1)), [])
