 # 백준 No.1654 랜선 자르기
"""
이분탐색
처음 입력에서 1부터 입력을 제일 큰 값을 기준으로 이분 탐색을 진행한다. 그렇게 되면 binary_search에서 이분 탐색의 mid 값은 index를 계산하는 것이 아닌 매개변수를 나타내게 된다. 따라사 mid값을 기준으로 line_list의 모든 값들에 나누고, 그 값을 기준으로 binary_search를 재귀호출 해준다. 이때, 가장 큰 값을 찾아야하므로 binary_search의 종료 조건에 마주칠 때까지 반복해준다.
"""
import sys
input = sys.stdin.readline

def binary_search(target, left, right):
  count = 0
  if left > right:
    return right

  mid = (left + right) // 2

  for line in line_list:
    count += line // mid
  
  if count >= target:
    # 더 긴 줄을 만들어야한다.
    return binary_search(target, mid + 1, right)
  else:
    return binary_search(target, left, mid - 1)

k, n = map(int, input().split())

line_list = []
for _ in range(k):
  line_list.append(int(input()))

left, right = 1, max(line_list)
print(binary_search(n, left, right))