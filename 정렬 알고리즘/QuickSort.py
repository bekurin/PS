# 퀵 정렬 알고리즘
# pivot값을 사용하여 분할 하여 정렬한다.
array = [1,5,4,6,7,8,9,3,2,]

def quickSort(array, start, end):
  if start >= end:
    return
  pivot = start
  left = start + 1
  right = end

  while left < right:
    while left <= end and array[left] <= array[pivot]:
      left += 1
    while right > start and array[right] >= array[pivot]:
      right -= 1
    
    if left > right:
      array[right], array[pivot] = array[pivot], array[right]
    else:
      array[left], array[right] = array[right], array[left]
  quickSort(array, start, right-1)
  quickSort(array, right + 1, end)

quickSort(array, 0, len(array)-1)
print(array)