# https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations
from math import sqrt

def solution(numbers):
    size = len(numbers)
    case = set()
    
    for i in range(size):
        new = map(int, map(''.join, permutations(numbers, i+1)))
        case.update(set(new))
    case = list(case)

    prime = [1 for _ in case]
        
    for i, num in enumerate(case):
        if num == 0 or num == 1:
            prime[i] = 0
        if not prime[i]: continue
            
        for j in range(2, int(sqrt(num))+1):
            if not num % j and num != j:
                prime[i] = 0
                break
    
    return len([1 for p in prime if p])