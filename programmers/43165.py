# https://programmers.co.kr/learn/courses/30/lessons/43165

def dfs(first, cnt, numbers, target):
    left = sum(numbers)
    
    if not numbers:
        if first == target: return cnt + 1
        else: return cnt
    
    cnt = dfs(first + numbers[0], cnt, numbers[1:], target)
    cnt = dfs(first - numbers[0], cnt, numbers[1:], target)
    
    return cnt

def solution(numbers, target):
    return(dfs(0, 0, numbers, target))