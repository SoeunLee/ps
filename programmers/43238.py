# https://programmers.co.kr/learn/courses/30/lessons/43238

# 시간 범위에서 n에 가까운 n 이상의 사람이 심사 받는 시간 찾기
def solution(n, times):
    left = 0
    right = n*max(times)
    
    while left < right:
        mid = (left + right) // 2 # left 범위에 mid 포함
        ppl = 0
        
        for t in times:
            ppl += mid // t
            
        if ppl < n:
            left = mid + 1
        else:
            right = mid
            
    return right