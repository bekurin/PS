# 백준 No.1764 듣보잡

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
