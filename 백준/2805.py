# 백준 No.2805 나무 자르기
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
  for tree in tree_list:
    value = tree - mid
    count += value if value > 0 else 0
  
  if count >= target:
    return binary_search(target, mid + 1, right)
  else:
    return binary_search(target, left, mid - 1)

n, m = map(int, input().split())
tree_list = list(map(int, input().split()))

left, right = 1, max(tree_list)
print(binary_search(m, left, right))