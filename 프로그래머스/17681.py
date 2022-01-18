# 프로그래머스 No.17681 [1차] 비밀지도
"""
배열, 진법 계산
1. arr1을 순환하며 이진법 배열로 바꿔준다. 이때, n에 맞게 자릿수를 채워준다.
2. arr2를 순환하며 이진법 배열로 바꿔준다. 이때, n에 맞게 자릿수를 채워준다.
3. 이중반복문을 사용하여 모든 이차원 배열의 값을 순환한다.
4. 3의 과정 중에 벽을 발견하면 temp에 "#"을 더해준다.
5. 3의 과정 중에 벽을 발견하지 못하면 temp에 " "을 더해준다.
6. answer에 temp를 추가해준다.
7. 3을 반복한다.
"""
def get_binary_list(number, n):
  base = ''
  print(number)
  while number > 0:
    number, mode = divmod(number,2)
    base += str(mode)

  if len(base) < n:
    while len(base) < n:
      base += '0'

  base = base[::-1]
  return list(map(int, base))

def solution(n, arr1, arr2):
  answer = []
  map1, map2 = [], []

  for num in arr1:
    map1.append(get_binary_list(num, n))
  for num in arr2:
    map2.append(get_binary_list(num, n))

  print(map1)
  print(map2)
  for i in range(n):
    temp = ""
    for j in range(n):
      if map1[i][j] == 1 or map2[i][j] == 1:
        temp += "#"
      else:
        temp += " "
    answer.append(temp)
  return answer

n = 6
arr1 = 	[46, 33, 33 ,22, 31, 50]
arr2 = 	[27 ,56, 19, 14, 14, 10]
print(solution(n, arr1, arr2))