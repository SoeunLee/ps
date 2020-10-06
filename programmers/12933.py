# https://programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    answer = 0

    n = sorted(list(str(n)), reverse=True)
    answer = int(''.join(n))

    return answer