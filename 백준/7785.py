# 백준 No.7785 회사에 있는 사람

import sys
input = sys.stdin.readline

n = int(input())
name_dict = {}

for _ in range(n):
  name, status = map(str, input().split())

  if name in name_dict and status == 'leave':
    name_dict[name] = 0
  else:
    name_dict[name] = 1

answer = []
for key, value in name_dict.items():
  if value == 1:
    answer.append(key)

answer.sort(reverse = True)
for item in answer:
  print(item)