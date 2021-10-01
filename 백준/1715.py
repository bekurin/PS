import heapq

n = int(input())

data = []
answer = 0

for _ in range(n):
  data.append(int(input()))

if n == 1:
  print(0)
else:
  heapq.heapify(data)
  
  while len(data) > 1:
    temp1 = heapq.heappop(data)
    temp2 = heapq.heappop(data)
    heapq.heappush(data, temp1+temp2)
    print(data)
    answer += temp1 + temp2
  print(answer)