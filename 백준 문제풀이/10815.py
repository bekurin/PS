# 백준 10815번 숫자 카드 (이진 탐색)
def BinarySearch(data, target, start, end):
  if start > end:
    return print(0, end=' ')
  mid = (start + end) // 2
  if data[mid] == target:
    return print(1, end=' ')
  elif data[mid] > target:
    return BinarySearch(data, target, start, mid-1)
  else:
    return BinarySearch(data, target, mid+1, end)

n = int(input())
data1 = list(map(int, input().split()))
m = int(input())
data2 = list(map(int, input().split()))

data1 = sorted(data1, reverse=False)

for i in range(m):
  BinarySearch(data1, data2[i], 0, n-1)