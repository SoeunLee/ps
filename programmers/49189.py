# https://programmers.co.kr/learn/courses/30/lessons/49189

from collections import defaultdict

def solution(n, edge):
    graph = defaultdict(set)

    for e in edge:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    
    dist = [50001 for _ in range(n+1)]
    dist[1] = 0
    queue = [(1, 0), ]
    
    while queue:
        u, d = queue.pop(0)
        
        for v in graph[u]:
            if dist[v] > d + 1:
                dist[v] = d + 1            
                queue.append((v, d + 1))
    
    max_d = max(dist[1:])
    return dist.count(max_d)