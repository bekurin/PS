# 이진 탐색 파이썬 코드
def BinarySearch(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  if array[mid] == target:
    return mid
  # 가운데 값이 목표값보다 작은 경우(가운데 기준 왼쪽 확인)
  elif array[mid] > target:
    return BinarySearch(array, target, start, mid-1)
  else:
    return BinarySearch(array, target, mid+1, end)

array = [1,2,3,4,5,6,7,8,9,10]
target = 5
result = BinarySearch(array, target, 0, 9)
print(result)