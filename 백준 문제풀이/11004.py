def MergeSort(array):
  if len(array) <= 1:
    return array
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

n, k = map(int, input().split())
array = list(map(int, input().split()))
array = MergeSort(array)
print(array[k-1])