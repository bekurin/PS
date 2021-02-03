# 계수 정렬 알고리즘
# 인덱스 번호를 이용한 정렬 알고리즘
# 범위가 작고 원소들이 양의 정수일 때 사용 가능
array = [1,5,4,6,7,8,9,3,2,]

count = [0] * (max(array)+1)

for i in range(len(array)):
  count[array[i]] += 1

for i in range(len(count)):
  for j in range(count[i]):
    print(i, end=' ')