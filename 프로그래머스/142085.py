# 프로그래머스 No.142085 디펜스 게임
from heapq import heappush, heappop

def solution(n, k, enemy):
  heap = []
  for idx, enemy_count in enumerate(enemy):
    heappush(heap, enemy_count)
    if len(heap) > k:
      n -= heappop(heap)
    if n < 0:
      return idx
  return len(enemy)

n = 7
k = 3
enemy = [4, 2, 4, 5, 3, 3, 1]
print(solution(n, k, enemy))
