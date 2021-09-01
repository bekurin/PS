# baekjoon No.1149 RGB 거리
n = int(input())
cost = []

for _ in range(n):
  cost.append(list(map(int, input().split(' '))))

# 3번 색을 칠한다.
for i in range(1, len(cost)):
  cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + cost[i][0]
  cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + cost[i][1]
  cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + cost[i][2]

print(min(cost[-1]))