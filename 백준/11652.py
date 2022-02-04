# 백준 No.11652 카드

import sys
input = sys.stdin.readline

n = int(input())
number_dict = {}

for _ in range(n):
  number = int(input())
  if number in number_dict:
    number_dict[number] += 1
  else:
    number_dict[number] = 1

answer = sorted(number_dict.items(), key = lambda x: (-x[-1],x[0]))
print(answer[0][0])