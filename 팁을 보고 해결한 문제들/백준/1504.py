# 백준 No.1504 특정한 최단 경로
"""
다익스트라, 그래프 이론
start -> v1 -> v2 -> n 경로와 start -> v2 -> v1 -> n 경로 2가지가 존재하므로 start, v1, v2 정점에서 시작하여 각각의 경로를 구해주고, 위 2가지 경로들의 거리를 계산해서 더 작은 값을 결과로 반환해준다. 만약 결과가 INF보다 크거나 같다면 -1을 결과로 반환한다.
"""
import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
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

INF = int(1e9)

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
  a, b, c = map(int, input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))

v1, v2 = map(int, input().split())

start_dist = dijkstra(1)
v1_dist = dijkstra(v1)
v2_dist = dijkstra(v2)

answer = min(start_dist[v1] + v1_dist[v2] + v2_dist[n], start_dist[v2] + v2_dist[v1] + v1_dist[n])
print(answer if answer < INF else -1)