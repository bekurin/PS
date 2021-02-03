# 병합 정렬 알고리즘
# 최악의 경우에도 O(NlogN)의 시간 복잡도를 보장한다.
array = [1,5,4,6,7,8,9,3,2,]

def MergeSort(array):
  if len(array) <= 1:
    return array
  print(array)
  mid = len(array) // 2
  left = MergeSort(array[:mid])
  right = MergeSort(array[mid:])
  i, j, k = 0, 0, 0

  while i < len(left) and j < len(right):
    if left[i] < right[i]:
      array[k] = left[i]
      i += 1
    else:
      array[k] = right[j]
      j += 1
    k += 1
  if i == len(left):
    while j < len(right):
      array[k] = right[j]
      j += 1
      k += 1
  elif j == len(right):
    while i < len(left):
      array[k] = left[i]
      i += 1
      k += 1
  return array

array = MergeSort(array)
print(array)
      