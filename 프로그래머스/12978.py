# 프로그래머스 No.12978 배달
import heapq
INF = int(1e9)

def get_graph(road, n):
    graph = [[] for _ in range(n+1)]

    for vertex, edge, cost in road:
        graph[vertex].append((edge, cost))
        graph[edge].append((vertex, cost))
    return graph


def dijkstra(start, graph, n):
    queue = []
    heapq.heappush(queue, (0, start))
    distance = [INF] * (n + 1)
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
    return distance

def solution(N, road, K):
    answer = 0
    for result in dijkstra(1, get_graph(road, N), N):
        if result <= K:
            answer += 1
    return answer

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
print(solution(N, road, K))