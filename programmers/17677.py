# https://programmers.co.kr/learn/courses/30/lessons/17677

def inter(a, b):
    result = 0
    _inter = set(a) & set(b)
    
    for i in _inter:
        result += min(a.count(i), b.count(i))
    
    return result
    
def union(a, b):
    result = 0
    _union = set(a) | set(b)
    
    for u in _union:
        result += max(a.count(u), b.count(u))
    
    return result
    
def fun(s):
    ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    size = len(s)
    result = []
    
    for i in range(size-1):
        if s[i] not in ABC or s[i+1] not in ABC: continue
        result.append(s[i]+s[i+1])
    
    return result

def solution(str1, str2):
    answer = 0
    
    str1 = fun(str1.upper())
    str2 = fun(str2.upper())
    
    if not str1 and not str2: answer = 1
    else: answer = inter(str1, str2) / union(str1, str2)
    
    return int(answer * 65536)