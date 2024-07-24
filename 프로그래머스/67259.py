# 프로그래머스 no.67259 경주로 건설
from collections import deque

def is_valid_move(nx, ny, n):
    return 0 <= nx < n and 0 <= ny < n

def is_blocked(board, nx, ny, n):
    return (nx, ny) == (0, 0) or not is_valid_move(nx, ny, n) or board[nx][ny] == 1

def calculate_cost(direction, prev_direction, cost):
    if prev_direction == -1 or (prev_direction - direction) % 2 == 0:
        return cost + 100
    else:
        return cost + 600

def shoudle_update(nx, ny, direction, new_cost, visited):
    return visited[nx][ny][direction] == 0 or visited[nx][ny][direction] > new_cost

def solution(board):
    answer = float("inf")
    queue = deque()
    queue.append((0, 0, -1, 0))
    n = len(board)

    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    visited = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(n)]

    while queue:
        x, y, prev_direction, cost = queue.popleft()

        for direction, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if is_blocked(board, nx, ny, n):
                continue
            new_cost = calculate_cost(direction, prev_direction, cost)

            if (nx, ny) == (n - 1, n - 1):
                answer = min(answer, new_cost)
            elif shoudle_update(nx, ny, direction, new_cost, visited):
                queue.append((nx, ny, direction, new_cost))
                visited[nx][ny][direction] = new_cost
    return answer

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(solution(board))
