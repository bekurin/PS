# 백준 No.2295 세 수의 합
"""
조합을 사용하여 세 수의 합을 구하고, number_list를 이진탐색을 실시하는 코드로 작성하였지만 세 수의 합을 구하기 위한 조합의 시간복잡도 O(N^3), 이진탐색 시간복잡도 O(logN) 따라서 위의 방법은 시간복잡도가 O(N^3longN)으로 통과하기 힘들다. 

따라서 target = a1 + a2 + a3 공식을 target - a3 = a1 + a2로 수정하여 접근하였다.
이렇게 하면 a1 + a2를 set에 넣는 연산 O(N^2) set에서 target의 값이 존재하는지 확인하는 연산(해쉬 테이블) O(1) 이므로 통합 시간복잡도 O(N^2)이 걸리므로 n의 최댓값 1000이므로 문제를 해결할 수 있습니다.

또 다른 방법으로는 target 값의 존재여부를 이진탐색으로 찾는 방법이 있습니다. 위의 공식을 그대로 이용하여 a1 + a2를 set에 넣는 연산 O(N^2), 이진탐색 시간복잡도 O(logN) 따라서 통합 시간복잡도 O(N^2longN)이 걸리므로 문제를 해결할 수 있습니다. 
"""
import sys
input = sys.stdin.readline

def binary_search(target, array, left, right):
  if left > right:
    return False

  mid = (left + right) // 2

  if array[mid] == target:
    return True
  elif array[mid] > target:
    # target exist on the left
    return binary_search(target, array, left, mid - 1)
  else:
    # target exist on the right
    return binary_search(target, array, mid + 1, right)

n = int(input())
number_list = []

for _ in range(n):
  number_list.append(int(input()))

two_sum = set()
for x in range(n):
  for y in range(x, n, 1):
    two_sum.add(number_list[x] + number_list[y])

# 메모리 72344KB 시간 3840ms
answer = 0
two_sum_list = sorted(list(two_sum))
for x in range(n):
  for y in range(x, n, 1):
    target = abs(number_list[y] - number_list[x])
    if binary_search(target, two_sum_list, 0, len(two_sum_list) - 1):
      # answer exist on the target elements
      answer = max(answer, number_list[x] if number_list[x] > number_list[y] else number_list[y])
print(answer)

# 메모리 64656KB 시간 512ms
answer = 0
for x in range(n):
  for y in range(x, n, 1):
    target = abs(number_list[y] - number_list[x])
    if target in two_sum:
      # answer exist on the target elements
      answer = max(answer, number_list[x] if number_list[x] > number_list[y] else number_list[y])
print(answer)