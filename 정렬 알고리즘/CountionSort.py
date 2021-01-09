array = [1,5,4,6,7,8,9,3,2,]

count = [0] * (max(array)+1)

for i in range(len(array)):
  count[array[i]] += 1

for i in range(len(count)):
  for j in range(count[i]):
    print(i, end=' ')