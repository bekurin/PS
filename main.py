def _1038(n, plus, array, rest):
  if n == -1:
    rest.append(plus)
    return
  _1038(n-1, plus, array, rest)
  _1038(n-1, (plus * 10) + n, array, rest)

arr = [0,1,2,3,4,5,6,7,8,9]
res = []

n = int(input())

if n >= 1023:
  print("-1")
else:
  _1038(9, 0, arr, res)
  res.sort()
  print(res[n+1])
print(res)