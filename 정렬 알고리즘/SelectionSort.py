# 선택 정렬 알고리즘
# 가장 간단하게 구현 가능한 알고리즘 배열을 탐색하여 가장 작은값과 검색 중인 인덱스의 값과 바꾸는 방식 사용
array = [1,5,2,3,4]

for i in range(len(array)):
  minIndex = i;
  for j in range(i+1, len(array)):
     if array[minIndex] > array[j]:
        minIndex = j
  array[i], array[minIndex] = array[minIndex], array[i]

print(array)