# https://programmers.co.kr/learn/courses/30/lessons/12931

def solution(n):
    answer = 0

    string = str(n)
    for s in string:
        answer += int(s)

    return answer