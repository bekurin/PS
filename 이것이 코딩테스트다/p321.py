n = list(input())
n = list(map(int, n))
data1 = n[:len(n)//2]
data2 = n[len(n)//2:]

if sum(data1) == sum(data2):
  print("LUCKY")
else:
  print("READY")