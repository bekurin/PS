# 백준 No.15663 N과 M(9) 
"""
백트래킹
"""
import sys
input = sys.stdin.readline

def dfs(index, numbers):
  global answer_set

  if len(numbers) == m:
    number_str = " ".join(map(str, numbers))

    if number_str not in answer_set:
      print(number_str)
      answer_set.add(number_str)
    return
  
  for i in range(len(number_list)):
    if i in index: continue
    
    numbers.append(number_list[i])
    index.append(i) 
    dfs(index, numbers)
    index.pop()
    numbers.pop()

n, m = map(int , input().split())
number_list = sorted(list(map(int, input().split())))

answer_set = set()
dfs([], [])