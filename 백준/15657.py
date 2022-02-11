# 백준 No.15657 N과 M(8)
"""
백트래킹
"""
import sys
input = sys.stdin.readline

def dfs(index, numbers):
  global answer_list

  if len(numbers) == m:
    answer_list.append(numbers[:])
    return
  
  for i in range(index, len(number_list)):
    numbers.append(number_list[i])
    dfs(i, numbers)
    numbers.pop()

n, m = map(int, input().split())
number_list = sorted(list(map(int, input().split())))

answer_list = []
dfs(0, [])

for answer in answer_list:
  for item in answer:
    print(item, end = " ")
  print("")