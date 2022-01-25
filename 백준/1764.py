# 백준 No.1764 듣보잡
"""
딕셔너리
1. 들어보지 못한 이름 목록을 딕셔너리에 저장한다.
2. 보지 못한 이름이 들어보지 못한 이름에 있으면 answer에 저장한다.
"""
answer = ['c','b','a']
n, m = map(int, input().split())
heard, seen = {}, {}

for _ in range(n):
  name = input()
  heard[name] = 1

for _ in range(m):
  name = input()
  if name in heard:
    answer.append(name)

print(len(answer))
for item in sorted(answer):
  print(item)
