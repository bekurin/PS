a, b = map(int, input().split())

data = []

count = 1
while len(data) <= 1000:
  for i in range(count):
    data.append(count)
  count += 1

data = data[(a-1):b]

answer = 0
for i in range(len(data)):
  answer += data[i]
print(answer)