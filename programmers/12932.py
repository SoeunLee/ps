# https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    answer = list(map(int, list(str(n)[::-1])))
    
    return answer