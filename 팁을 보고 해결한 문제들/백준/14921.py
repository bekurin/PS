# 백준 No.14921 용액 합성하기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def binary_search(target, left, right):
  if left >= right:
    return target
  
  answer = data_list[left] + data_list[right]

  if abs(target) > abs(answer):
    target = answer

  if answer < 0:
    return binary_search(target, left + 1, right)
  else:
    return binary_search(target, left, right - 1)

n = int(input())
data_list = list(map(int, input().split()))
print(binary_search(float('inf'), 0, n - 1))