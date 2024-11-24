# 프로그래머스 no.62050 지형 이동
from heapq import heappush, heappop

def solution(land, height):
    answer = 0
    n = len(land)
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False] * n for _ in range(n)]
    
    queue = []
    heappush(queue, [0, 0, 0])
    
    while queue:
        cost, y, x = heappop(queue)
        
        if not visited[y][x]:
            visited[y][x] = True
            answer += cost
            
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                
                if 0 <= ny < n and 0 <= nx < n:
                    temp_cost = abs(land[y][x] - land[ny][nx])
                    if temp_cost > height:
                        new_cost = temp_cost
                    else:
                        new_cost = 0
                    heappush(queue, [new_cost, ny, nx])
    return answer
