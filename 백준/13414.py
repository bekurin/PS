# 백준 No.13414 수강신청
"""
해시, 딕셔너리, 자료구조
처음 문제를 접근할 때에는 큐를 사용하여 해결하려고 하였지만 큐에서 number 값을 찾는 시간과 remove를 하는 시간이 오래 걸려서 시간 초과가 나왔다.

따라서 딕셔너리에 마지막에 들어온 시간을 초기화해주고, 시간을 기준으로 정렬하여 k개만큼의 답을 출력하는 것으로 문제를 해결했다.
"""
import sys

input = sys.stdin.readline

# 성공한 해결 방법
k, l = map(int, input().split())
answer_dict = {}

for i in range(l):
  number = input().strip()
  answer_dict[number] = i
    
for i, answer in enumerate(sorted(list(answer_dict.items()), key = lambda x: x[-1])):
  if i >= k:
    break
  print(answer[0])

# 첫번째 해결 방법
from collections import deque

k, l = map(int, input().split())
answer = deque()

for _ in range(l):
  number = input()
  if number in answer:
    answer.remove(number)
    answer.append(number)
  else:
    answer.append(number)

result_list = sorted(list(answer)[:k])
for result in result_list:
  print(result)