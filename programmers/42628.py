# https://programmers.co.kr/learn/courses/30/lessons/42628

def solution(operations):
    answer = []

    queue = []
    while operations:
        op = operations.pop(0)
        op = op.split(' ')

        if op[0] == 'I':
            queue.append(int(op[1]))
            queue = sorted(queue)   # 오름차순

        elif not queue: continue
        elif int(op[1]) < 0: queue.pop(0)
        else: queue.pop(-1)

    if not queue:
        return [0, 0]

    return [queue[-1], queue[0]]