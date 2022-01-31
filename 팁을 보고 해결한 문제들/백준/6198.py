# 백준 No.6198 옥상 정원 꾸미기
"""
stack에 건물들을 저장한다. stack에서 값을 하나씩 확인하며 현재 건물보다 작은 건물들을 삭제한다. (볼 수 없는 건물이기 때문에)

현재 건물이 뭘 볼 수 있는지를 확인하는 방향이 아니라 현재 건물을 볼 수 있는 건물들을 확인하는 방향으로 접근해야한다.
"""
import sys
input = sys.stdin.readline

def solution(tower_list, n):
  answer = 0
  stack = []

  for i, tower in enumerate(tower_list):
    print(i, tower, stack, end = " ")
    while stack and stack[-1] <= tower:
      stack.pop()
    stack.append(tower)
    answer += len(stack) - 1
    print(answer)
  return answer

# n = int(input())
# tower_list = []

# for _ in range(n):
#   tower_list.append(int(input()))
# print(solution(tower_list[::-1], n))

tower_list = [10,3,2,4,12,2]
n = len(tower_list)
print(solution(tower_list, n))