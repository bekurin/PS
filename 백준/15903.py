# 백준 No.15903 카드 합체 놀이
"""
자료 구조, 그리디 알고리즘, 우선순위 큐

힙의 크기가 2 이상일 경우에 pop()을 사용하여 작은 값 2개로 꺼내주어 더한 값을 다시 힙에 넣어준다.
"""
import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
number_list = list(map(int, input().split()))

heap = []
for number in number_list:
  heapq.heappush(heap, number)

for _ in range(m):
  if len(heap) >= 2:
    number_sum = 0
    for _ in range(2):
      number_sum += heapq.heappop(heap)

    for _ in range(2):
      heapq.heappush(heap, number_sum)
print(sum(heap))