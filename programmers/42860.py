# https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    idx_A = []
    size = len(name)
    answer = 0
    move = size-1
    
    for a in name:
        idx = ABC.index(a)
        if idx > 13:
            idx = 26-idx
        answer += idx
    
    for i, a in enumerate(name):
        if a == "A": idx_A.append(i)
    
    for i in idx_A:
        a = list(name[:i])
        b = list(name[i+1:])
        
        while a and a[-1] == "A":
            a.pop()
        while b and b[0] == "A":
            b.pop(0)
        
        a = ''.join(a)
        b = ''.join(b)
        len_a = max(len(a)-1, 0)
        len_b = len(b)
        
        move = min(move, len_a*2+len_b, len_a+len_b*2)
        
    return answer + move