n = int(input())

moneyTypes = list(map(int, input().split()))
moneyTypes = sorted(moneyTypes, reverse=False)

target  = 1
for i in moneyTypes:
  if target < x:
    break
  target += x