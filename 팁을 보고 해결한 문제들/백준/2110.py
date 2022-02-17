# 백준 No.2110 공유기 설치
"""
이분 탐색, 매개 변수 탐색
"""
import sys
input = sys.stdin.readline

def binary_search(left, right):
  global answer

  if left > right: return

  # 공유기 사이의 최소 거리
  mid = (left + right) // 2
  target, current = 1, house_list[0]

  for house in house_list:
    # 유효한 거리에 있는지 확인하는 조건
    if house >= current + mid:
      target += 1
      current = house

  if target >= c:
    # 공유기의 거리가 너무 작기 때문에 넓게 해준다.
    answer = mid
    return binary_search(mid + 1, right)
  else:
    # 공유가의 거리가 너무 넓기 때문에 작게 해준다.
    return binary_search(left, mid - 1)
    
n, c = map(int, input().split())

house_list = []
for _ in range(n):
  house_list.append(int(input()))
house_list.sort()

left, right, answer = 1, house_list[-1] - house_list[0], 0
binary_search(left, right)
print(answer)