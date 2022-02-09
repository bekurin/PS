# 백준 No.15655 N과 M(6)
import sys
input = sys.stdin.readline

def combination(index, numbers):

  if len(numbers) == m:
    answer_list.append(numbers[:])
    return

  for i in range(index, len(number_list)):
    numbers.append(number_list[i])
    combination(i + 1, numbers)
    numbers.pop()

n, m = map(int, input().split())
number_list = sorted(map(int, input().split()))

answer_list = []
combination(0, [])

for answer in answer_list:
  for item in answer:
    print(item, end =" ")
  print("")