n = list(input())

count0 = 0
count1 = 0

for i in range(len(n)-1):
  if n[i] != n[i+1]:
    if n[i] == '1':
      count0 += 1
    else:
      count1 += 1

if count0 > count1:
  print(count1)
else:
  print(count0)