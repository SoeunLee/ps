# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    result = [0 for _ in prices]

    queue = []
    for i, now in enumerate(prices):
        _queue = []
        while queue:
            j, top = queue.pop(0)
            if top > now:
                result[j] = i-j
            else:
                _queue.append((j, top))

        queue = _queue[:]
        queue.append((i, now))
    
    size = len(prices)
    for i, val in enumerate(result):
        if not val:
            result[i] = size-i-1
            
    return result