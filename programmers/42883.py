# https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    answer = ''
    box = []
    
    for n in number:
        while box and box[-1] < n and k > 0:
            k -= 1
            box.pop(-1)
        box.append(n)
    
    if k > 0: box = box[:len(box) - k]
    answer = ''.join(box)
    
    return answer