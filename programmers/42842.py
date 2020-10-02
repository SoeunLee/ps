# https://programmers.co.kr/learn/courses/30/lessons/42842

from math import sqrt

def solution(brown, yellow):
    answer = []
    stop = int(sqrt(yellow)) + 1
    
    queue = []
    for i in range(1, stop):
        if yellow % i == 0:
            queue.append((yellow//i, i))
    
    for q in queue:
        if brown == q[0]*2 + q[1]*2 + 4:
            return [q[0]+2, q[1]+2]