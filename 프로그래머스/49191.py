# 프로그래머스 No.49191 순위
from collections import deque


def get_graph(n, results):
    graph = [[] for _ in range(n + 1)]
    for vertex, edge in results:
        graph[vertex].append(edge)
    return graph


def bfs(start, graph, visited, win_lose_list):
    queue = deque()
    queue.append(start)

    visited[start] = True

    while queue:
        vertex = queue.popleft()
        for item in graph[vertex]:
            if not visited[item]:
                queue.append(item)
                win_lose_list[start][0] += 1
                win_lose_list[item][1] += 1
                visited[item] = True
    return win_lose_list


def solution(n, results):
    answer, win_lose_list = [], [[0, 0] for _ in range(n + 1)]
    graph = get_graph(n, results)

    for start in range(1, n + 1):
        visited = [False] * (n + 1)
        win_lose_list = bfs(start, graph, visited, win_lose_list)

    answer = list(map(lambda item: 1 if sum(item) == (n-1) else 0, win_lose_list))
    return sum(answer)


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))