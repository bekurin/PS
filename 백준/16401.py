# 백준 No.16401 과자 나눠주기
"""
이분 탐색, 매개 변수 탐색
"""
import sys
input = sys.stdin.readline

def binary_search(target, left, right):

  if left > right:
    return right

  mid = (left + right) // 2

  count = 0
  for snack in snack_list:
    count += snack // mid
  
  if count >= target:
    # 더 큰 과자
    return binary_search(target, mid + 1, right)
  else:
    return binary_search(target, left, mid - 1)

m, n = map(int, input().split())
snack_list = list(map(int, input().split()))

left, right = 1, max(snack_list)
print(binary_search(m, left, right))