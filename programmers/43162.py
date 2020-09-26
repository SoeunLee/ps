# https://programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    visit = [0 for _ in range(n)]
    net = 1
    
    while 0 in visit:
        root = visit.index(0)
        queue = [root, ]
        while queue:
            top = queue.pop(0)
            if visit[top]:
                continue

            visit[top] = net
            for i in range(n):
                if i == top: continue
                if computers[top][i]:
                    queue.append(i)
        net += 1

    return len(set(visit))