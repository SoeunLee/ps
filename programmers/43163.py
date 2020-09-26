# https://programmers.co.kr/learn/courses/30/lessons/43163

def replace(src, i, X):
    dst = list(src[:])
    dst[i] = X
    return str(dst)

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    visit = [ -1 for _ in words ]
    length = len(begin)
        
    queue = [(begin, 0), ]
    while queue:
        top, cnt = queue.pop(0)
        
        if top in words:
            idx = words.index(top)
            if visit[idx] >= 0:
                continue
            visit[idx] = cnt
            
        for i in range(length):
            _top = replace(top, i, 'X')
            
            for word in words:
                _word = replace(word, i, 'X')
                if _top == _word:
                    queue.append((word, cnt+1))
    
    return visit[words.index(target)]