# 백준 No.15656 N과 M(7)
import sys
input = sys.stdin.readline

def permutation(numbers):

  if len(numbers) == m:
    answer_list.append(numbers[:])
    return

  for i in range(0, len(number_list)):
    numbers.append(number_list[i])
    permutation(numbers)
    numbers.pop()

n, m = map(int, input().split())
number_list = sorted(map(int, input().split()))

answer_list = []
permutation([])

for answer in answer_list:
  for item in answer:
    print(item, end =" ")
  print("")