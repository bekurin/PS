# 프로그래머스 no.92343 양과 늑대
from collections import deque

def solution(info, edges):
    tree = build_tree(info, edges)
    max_sheep = 0
    
    queue = deque([(0, 1, 0, set())])
    
    while queue:
        current, sheep_count, wolf_count, visited_nodes = queue.popleft()
        max_sheep = max(max_sheep, sheep_count)
        visited_nodes.update(tree[current])
        
        for next_node in visited_nodes:
            if info[next_node]:
                if sheep_count != wolf_count + 1:
                    queue.append((next_node, sheep_count, wolf_count + 1, visited_nodes - {next_node}))
            else:
                queue.append((next_node, sheep_count + 1, wolf_count, visited_nodes - {next_node}))
    return max_sheep

def build_tree(info, edges):
    tree = [[] for _ in range(len(info))]
    for edge in edges:
        tree[edge[0]].append(edge[1])
    return tree
