# 프로그래머스 no.159993 미로 탈출
from collections import deque

def is_valid_move(ny, nx, n, m, maps):
    return 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != "X"

def append_queue(ny, nx, k, time, visited, queue):
    if not visited[ny][nx][k]:
        visited[ny][nx][k] = True
        queue.append((ny, nx, k, time + 1))

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]
    
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    queue = deque()
    destination_y, destination_x = -1, -1
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                queue.append((i, j, False, 0))
            if maps[i][j] == "E":
                destination_y, destination_x = i, j
    
    while queue:
        y, x, is_pull_lever, time = queue.popleft()
        
        if y == destination_y and x == destination_x and is_pull_lever:
            return time
    
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            
            if not is_valid_move(ny, nx, n, m, maps):
                continue
                
            if maps[ny][nx] == "L":
                append_queue(ny, nx, True, time, visited, queue)
            else:
                append_queue(ny, nx, is_pull_lever, time, visited, queue)
    return -1             
