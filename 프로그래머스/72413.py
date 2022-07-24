# 프로그래머스 No.72413 합승 택시 요금
import heapq
INF = int(1e9)


def solution(n, s, a, b, fares):
    answer = INF
    graph = get_graph(fares, n)

    share_distance = dijkstra(s, graph, n)
    for start in range(1, n + 1):
        distance = dijkstra(start, graph, n)
        answer = min(answer, share_distance[start] + distance[a] + distance[b])
    return answer


def get_graph(fares, n):
    graph = [[] for _ in range(n + 1)]
    for vertex, edge, cost in fares:
        graph[vertex].append((edge, cost))
        graph[edge].append((vertex, cost))
    return graph


def dijkstra(start, graph, n):
    queue = []
    distance = [INF] * (n + 1)
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue

        for item in graph[now]:
            cost = dist + item[-1]
            if cost < distance[item[0]]:
                distance[item[0]] = cost
                heapq.heappush(queue, (cost, item[0]))
    return distance


n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))
