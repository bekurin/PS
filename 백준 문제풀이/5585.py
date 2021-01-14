# 백준 5585번 거스름 돈(그리디)
n = (int(input()))
n = 1000 - n
moneyTypes = [500, 100, 50, 10, 5, 1]
count = 0

while n != 0:
  for i in moneyTypes:
    count += n // i
    n %= i
print(count) 