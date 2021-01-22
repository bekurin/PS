n = input()

length = len(n)
n = int(n)

data = []
for _ in range(length):
  data.append(n % 10)
  n //= 10

length //= 2

dataLeft = data[length:]
dataRight = data[:length]
sumleft, sumright = 0, 0

for i in range(length):
  sumleft += dataLeft[i]
  sumright += dataRight[i]

if sumleft == sumright:
  print("LUCKY")
else:
  print("READY")
