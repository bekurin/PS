# 백준 No.2230 수 고르기
import sys
input = sys.stdin.readline

def two_pointer(target, left, right):
  answer = float('inf')

  while left < n and right < n:
    diff = data_list[right] - data_list[left]

    if diff == target: return target
    elif diff < target:
      right += 1
    else:
      answer = min(answer, diff)
      left += 1
  return answer

n, m = map(int, input().split())
data_list = []
for _ in range(n):
  data_list.append(int(input()))
data_list.sort()

print(two_pointer(m, 0, 1))