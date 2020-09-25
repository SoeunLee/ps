# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    left = []
    
    for i, p in enumerate(progresses):
        v = (100 - p) // speeds[i]
        if (100 - p) % speeds[i] > 0:
            v += 1
        left.append(v)
    
    for day in range(1, 100):
        cnt = 0
        while left:
            if left[0] > day:
                break
            left.pop(0)
            cnt += 1
        if cnt > 0:
            answer.append(cnt)
    
    return answer