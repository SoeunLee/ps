# https://programmers.co.kr/learn/courses/30/lessons/43164

from collections import defaultdict

def dfs(dest, route, remain):
    if len(remain) == 0:
        return route
    
    result = []
    last = route[-1]
    
    for d in dest[last]:
        if (last, d) not in remain: continue
        x = remain.index((last, d))
        r = dfs(dest, route+[d,], remain[:x] + remain[x+1:])
        
        if not r: continue
        result.append(r)
    
    while result and type(result[0]) == list:
        result = min(result)
    return result

def solution(tickets):
    tickets = sorted(list(map(tuple, tickets)))
    dest = defaultdict(list)
    
    for t in tickets:
        dest[t[0]].append(t[1])
    
    return dfs(dest, ["ICN",], tickets)