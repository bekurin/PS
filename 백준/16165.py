# 백준 No.16165 걸그룹 마스터 준석이
n, m = map(int, input().split())

group_dict = {}
name_dict = {}
for _ in range(n):
  group_name = input()
  k = int(input())

  group_dict[group_name] = []
  for _ in range(k):
    name = input()
    name_dict[name] = group_name
    group_dict[group_name].append(name)
  
for _ in range(m):
  name = input()
  quiz_type = int(input())

  if quiz_type == 1:
    print(name_dict[name])
  else:
    for value in sorted(group_dict[name]):
      print(value)