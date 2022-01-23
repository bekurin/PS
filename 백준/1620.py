# 백준 No.1620 나는야 포켓몬 마스터 이다솜
"""
해쉬
1. 포켓몬의 이름을 key로 순서는 value로 저장하는 pokemon_dict
2. 포켓몬 순서를 value로 이름을 key로 저장하는 number_dict
를 각각 생성하여 검색해준다. dict의 검색 시간복잡도 O(1)
"""

def solution(target,pokemon_dict, number_dict):
  if target.isdigit():
    print(number_dict[int(target)])
  else:
    print(pokemon_dict[target])

n, m = map(int, input().split())

pokemon_dict, number_dict = {}, {}
for i in range(n):
  name = input()
  pokemon_dict[name] = i+1
  number_dict[i+1] = name

for _ in range(m):
  target = input()
  solution(target,pokemon_dict, number_dict)