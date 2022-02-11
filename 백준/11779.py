# 백준 No.11779 최소비용 구하기 2
"""
다익스트라, 그래프 이론
heapq에 경로도 같이 넣어주면 현재 탐색하고 있는 노드를 포함시킬지 여부를 판단하지 않고 경로를 계산할 수 있다.
"""
import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

def dijkstra(start):
  q = []
  distance = [INF] * (n + 1)
  distance[start] = 0
  heapq.heappush(q, (0, start, [start]))

  while q:
    dist, now, path = heapq.heappop(q)

    if distance[now] < dist:
      continue
    
    for vertex, edge in graph[now]:
      cost = dist + edge

      if cost < distance[vertex]:
        distance[vertex] = cost
        route[vertex] = path + [vertex]
        heapq.heappush(q, (cost, vertex, path + [vertex]))
  return distance

n = int(input())
m = int(input())

route = [[] for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b,c))
start, end = map(int, input().split())

distance = dijkstra(start)

print(distance[end])
print(len(route[end]))
for item in route[end]:
  print(item, end = " ")