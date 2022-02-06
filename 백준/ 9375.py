# 백준 No.9375 패션왕 신해빈
"""
딕셔너리, 조합론
category와 item을 딕셔너리에 저장하고, 몇개의 조합이 나오는지를 확인하는 방향으로 코드를 작성하였는데 시간 초과가 나왔다.

정답 코드는 category에 저장된 item의 개수를 모두 곱한 것에서 옷을 입지 않은 경우를 빼주는 것을 사용하여 작성한 코드이다. 
"""
import sys
input = sys.stdin.readline

# 정답 코드
t = int(input())
for _ in range(t):
  n = int(input())
  answer = 1
  item_dict = {}

  for _ in range(n):
    item, category = input().split()

    if category in item_dict:
      item_dict[category].append(item)
    else:
      item_dict[category] = [item]

  for key, value in item_dict.items():
    answer *= len(value) + 1
  print(answer - 1)

# 시간 초과 코드
def combination(index, items):
  global answer

  if len(items) == len(item_dict):
    return

  for i in range(index, len(key_list)):
    for item in item_dict[key_list[i]]:
      items.append(item)
      answer += 1
      combination(i + 1, items)
      items.pop()

t = int(input())

answer = 0
item_dict, key_list = {}, []
for _ in range(t):
  n = int(input())
  answer = 0
  item_dict, key_list = {}, []

  for _ in range(n):
    item, category = input().split()

    if category in item_dict:
      item_dict[category].append(item)
    else:
      item_dict[category] = [item]

  key_list = list(item_dict.keys())
  combination(0, [])
  print(answer)