n = int(input())
data = []
for _ in range(n**2):
  data.append(list(map(int, input().split())))

data.sort()
times = 0

for i in range(len(data)):
  times = max(times, max(data[i]))

take = [False] * times
answer = 0
for i in range(times):
  for j in range(data[-1]):
    take[data[-1][i]] = True
    answer += data[-1][i]

print(answer)