n = list(input())

result = []
value = 0
for i in n:
  if i.isalpha():
    result.append(i)
  else:
    value += int(i)
result.sort()

for i in result:
  print(i, end='')
print(value)