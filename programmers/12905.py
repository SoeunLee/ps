# https://programmers.co.kr/learn/courses/30/lessons/12905

def solution(board):
    answer = 0
    
    for i, _board in enumerate(board):
        for j, val in enumerate(_board):
            if not i or not j or not val: continue
            board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
            
    answer = max(list(map(max, board)))
            
    return answer ** 2