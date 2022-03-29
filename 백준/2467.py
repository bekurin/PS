# 백준 No.2467 용액
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

answer = []
def binary_search(target, left, right):
  global answer
  if left >= right: return answer
  
  fusion = data_list[left] + data_list[right]
  
  if abs(target) > abs(fusion):
    target = fusion
    answer = [data_list[left], data_list[right]]

  if fusion < 0:
    return binary_search(target, left + 1, right)
  else:
    return binary_search(target, left, right - 1)

n = int(input())
data_list = list(map(int, input().split()))

answer = binary_search(float('inf'), 0, n-1)
print(answer[0], answer[1])