# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    cnt = len(lost)
    
    for i in lost:
        if i not in reserve: continue
            
        reserve.pop(reserve.index(i))
        lost[lost.index(i)] = -1
        cnt -= 1
            
    for i in lost:
        if i < 0: continue
            
        if i+1 in reserve:
            reserve.pop(reserve.index(i+1))
            cnt -= 1
            
        elif i-1 in reserve:
            reserve.pop(reserve.index(i-1))
            cnt -= 1
    
    return n - cnt