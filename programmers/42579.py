# https://programmers.co.kr/learn/courses/30/lessons/42579

from functools import reduce
from collections import defaultdict

def solution(genres, plays):
    answer = []
    album = defaultdict(list)
    
    for i, g in enumerate(genres):
        album[g].append((i, plays[i]))
    
    best = []
    for key, value in album.items():      
        selected = sorted(value, key=(lambda x: x[1]), reverse=True)
        sum = reduce((lambda a, b: a + b[1]), selected, 0)
        
        if len(selected) > 2:
            selected = selected[:2]
        
        best.append((sum, selected))
        
    best = sorted(best, reverse=True)
    
    for sum, selected in best:
        for s in selected:
            answer.append(s[0])

    return answer