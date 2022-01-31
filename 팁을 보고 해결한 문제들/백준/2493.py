# 백준 No.2493 탑
"""
stack
앞에서부터 차례로 순환하면 stack에 저장한다. 이때, 현재 tower의 값보다 큰 값이 stack에 저장되어 있다면 stack을 비워주고 answer의 값을 초기화해준다.
* 높은 건물이 찾아지면 이전 건물들에 대한 비교는 무의미하다. 
"""
import sys
input = sys.stdin.readline

# n = int(input())
# stack = list(map(int, input().split()))

# tip_solution
tower_list = [6, 9, 5, 7, 4]
stack = []
n = len(tower_list)

answer = [0] * n
for i, tower in enumerate(tower_list):
  while stack:
    if stack[-1][1] > tower:
      answer[i] = stack[-1][0] + 1
      break
    stack.pop()
  stack.append([i, tower])

print(" ".join(list(map(str,answer))))

"""
뒤에서부터 차례로 순환하여 n * (n + 1) / 2번의 비교를 수행한다. 현재 비교를 수행하는 tower만을 stack에서 지워준다.
"""
# my_solution
stack = [6, 9, 5, 7, 4]
answer = [0] * n
for i in range(n-1, -1, -1):
  current = stack.pop()
  stack_copy = stack.copy()

  while stack_copy:
    if current <= stack_copy[-1]:
      answer[i] = len(stack_copy)
      break
    stack_copy.pop()
    
print(" ".join(list(map(str,answer))))