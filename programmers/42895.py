# https://programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    note = []   # note[i] = { N * i개로 만드는 수 }
    
    if N == number:
        return 1
    
    for i in range(1, 9):
        note.append({int(str(N) * i)})

    for i in range(1, 8):
        for j in range(i):
            for a in note[j]:
                for b in note[(i-1)-j]:
                    note[i].add(a + b)
                    note[i].add(a - b)
                    note[i].add(a * b)
                    
                    if b != 0:
                        note[i].add(a // b)      
                        
        if number in note[i]:
            return i+1
        
    return -1