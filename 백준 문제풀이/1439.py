# 백준 1439번 뒤집기(그리디)
data = input()
count0, count1 = 0, 0

if data[0] == '1':
  count0 += 1
else:
  count1 += 1

for i in range(len(data)-1):
  if data[i] != data[i+1]:
    if data[i+1] == '1':
      count0 += 1
    else:
      count1 += 1

if count0 > count1:
  print(count1)
else:
  print(count0)