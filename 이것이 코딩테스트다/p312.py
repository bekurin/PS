data = input()

result = int(data[0])

for i in range(1, len(data)):
  num = int(data[i])
  if num == 0:
    result += num
  else:
    result *= num
print(result)