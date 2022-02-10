# 백준 No.11404 플로이드
"""
플로이드 와샬, 다익스트라
플로이드 와샬 알고리즘으로 구현해야하는 문제이지만 다익스트라를 사용하여 구현하습니다.
"""
import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
def dijstra(start):
  q = []
  distance = [INF] * (n + 1)
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue
    
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
  return distance

def replace_INF_to_0(distance):
  for i in range(len(distance)):
    if distance[i] == INF:
      distance[i] = 0
  return distance

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

for start in range(1, n+1):
  for item in replace_INF_to_0(dijstra(start)[1:]):
    print(item, end = " ")
  print("")