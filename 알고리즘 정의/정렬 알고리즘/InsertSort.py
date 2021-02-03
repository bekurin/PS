# 삽입 정렬 알고리즘
# 배열이 정렬 되어있다는 가정을 한다.
array = [1,5,2,3,4]

for i in range(1, len(array)):
  for j in range(i,0,-1):
    if array[j] < array[j-1]:
      array[j], array[j-1] = array[j-1], array[j]
    else:
      break

print(array)