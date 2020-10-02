# https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    answer = 0
    
    queue = []
    for idx, val in enumerate(priorities):
        queue.append((val, idx))
    
    result = []
    while queue:
        val = max(queue, key=(lambda x: x[0]))
        idx = queue.index(val)
        
        result.append(val)
        queue.pop(idx)
        
        if idx < len(queue):
            queue = queue[idx:] + queue[:idx]
        
    for r in result:
        if r[1] == location:
            return result.index(r) + 1