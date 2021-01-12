# 순차 탐색 알고리즘(선형 탐색)
def SequentialSearch(n, target, array):
  for i in range(n):
    if target == array[i]:
      return i + 1

array = [7,6,8,5,4,1,3,2]
target = int(input())

print(SequentialSearch(len(array), target, array))