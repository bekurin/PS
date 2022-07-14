# 프로그래머스 No.86971 전력망 둘로 나누기
from collections import deque


def bfs(start, graph, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        vertex = queue.popleft()

        for v in graph[vertex]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
    return visited.count(True)


def get_graph(n, wires):
    graph = [[] for _ in range(n + 1)]

    for vertex, edge in wires:
        graph[vertex].append(edge)
        graph[edge].append(vertex)
    return graph


def solution(n, wires):
    answer = 200
    graph = get_graph(n, wires)

    for vertex, edge in wires:
        graph[vertex].remove(edge)
        graph[edge].remove(vertex)

        visited = [False for _ in range(n + 1)]
        count = bfs(vertex, graph, visited)
        answer = min(answer, abs(n - count * 2))

        graph[vertex].append(edge)
        graph[edge].append(vertex)

    return answer


n = 9
wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]
print(solution(n, wires))
