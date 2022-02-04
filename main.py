# 백준 No.15651 N과 M(3)

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
