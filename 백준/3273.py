# 백준 No.3273 두 수의 합

import sys

input = sys.stdin.readline

# n = int(input())
# number_list = list(map(int, input().split()))
# target = int(input())

n = 9
number_list = [5,12,7,10,9,1,2,3,11]
target = 13

two_sub = [0] * n
answer = 0
for i in range(n):
  two_sub[i] = target - number_list[i]

number_set = set(number_list)
for number in two_sub:
  if number in number_set:
    answer += 1

print(answer // 2)