n = int(input())
data = list(map(int,input().split()))
data.sort()
result = []
distance = 0
minValue = -1

for i in range(n):
  for j in range(n):
    if distance > minValue:
      continue
    if i != j:
      distance += abs(data[j] - data[i])
  result.append([distance, data[i]])
  minValue = distance
  distance = 0

result.sort()
print(result[0][1])