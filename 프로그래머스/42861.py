# 프로그래머스 no.42861 섬 연결하기 
def find(parent, i):
    if parent[i] == i:
        return i
    parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)
    
    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

def solution(n, costs):
    costs.sort(key = lambda x: x[2])
    
    parent = [i for i in range(n)]
    rank = [0] * n
    
    min_cost, edges = 0, 0
    
    for edge in costs:
        if edges == n - 1:
            break
        x = find(parent, edge[0])
        y = find(parent, edge[1])
        
        if x != y:
            union(parent, rank, x, y)
            min_cost += edge[2]
            edges += 1
    return min_cost
