'''
sample_input

5
20 3
2 2 3 2 2 2 2 3 3 4 4 3 2 2 3 3 3 2 2 3
4 4 1 4 4 1 4 4 1 1 1 4 1 4 3 3 3 3 3 3
4 4 1 100
7 10 3 40
6 3 2 70
40 2
0 3 0 3 3 2 2 1 0 4 1 3 3 3 0 3 4 1 1 3 2 2 2 2 2 0 2 3 2 2 3 4 4 3 3 3 2 0 4 4 
0 1 0 3 4 0 4 0 0 1 1 1 0 1 4 4 4 4 4 3 3 3 0 1 0 4 3 2 1 4 4 3 2 3 2 2 0 4 2 1 
5 2 4 140
8 3 3 490
60 4
0 3 3 3 0 1 2 2 2 1 2 2 3 3 4 4 0 3 0 1 1 2 2 3 2 2 3 2 2 0 3 0 1 1 1 4 1 2 3 3 3 3 3 1 1 4 3 2 0 4 4 4 3 4 0 3 3 0 3 4 
1 1 4 1 1 1 1 1 1 4 4 1 2 2 3 2 4 0 0 0 4 3 3 4 3 3 0 1 0 4 3 0 4 3 2 3 2 1 2 2 3 4 0 2 2 1 0 0 1 3 3 1 4 4 3 0 1 1 1 1 
6 9 1 180
9 3 4 260
1 4 1 500
1 3 1 230
80 7
2 2 2 2 2 2 0 2 2 0 4 0 2 3 3 2 3 3 0 3 3 3 4 3 3 2 1 1 1 0 4 4 4 1 0 2 2 2 1 1 4 1 2 3 4 4 3 0 1 1 0 3 4 0 1 2 2 2 1 1 3 4 4 4 4 4 4 3 2 1 4 4 4 4 3 3 3 0 3 3 
4 4 1 1 2 1 2 3 3 3 4 4 4 4 4 1 1 1 1 1 1 1 1 0 3 3 2 0 4 0 1 3 3 3 2 2 1 0 3 2 3 4 1 0 1 2 2 3 2 0 4 0 3 4 1 1 0 0 3 2 0 0 4 3 3 4 0 4 4 4 4 0 3 0 1 1 4 4 3 0 
4 3 1 170
10 1 3 240
10 5 3 360
10 9 3 350
9 6 2 10
5 1 4 350
1 8 2 450
100 8
2 2 3 2 0 2 0 3 3 1 2 2 2 2 3 3 0 4 4 3 2 3 4 3 3 2 3 4 4 4 2 2 2 0 2 2 4 4 4 4 1 1 1 2 2 2 4 3 0 2 3 3 4 0 0 1 1 4 1 1 1 1 2 2 1 1 3 3 3 0 3 2 3 3 0 1 3 3 0 1 1 3 3 4 0 4 1 1 2 2 4 0 4 1 1 2 2 1 1 1 
4 4 4 0 4 1 1 4 1 1 1 1 3 2 1 2 1 1 4 4 1 0 2 3 4 4 4 4 4 0 1 0 2 2 2 0 2 2 2 2 2 2 3 0 0 1 4 3 3 2 0 0 4 4 4 0 2 0 4 1 1 2 2 0 4 4 0 0 2 0 2 3 3 0 2 3 0 3 4 0 4 3 4 4 3 4 1 1 2 2 2 0 0 1 0 4 1 1 1 4 
3 4 2 340
10 1 1 430
3 10 4 10
6 3 4 400
7 4 1 80
4 5 1 420
4 1 2 350
8 4 4 300

'''

'''
sample_output

#1 1200
#2 3290
#3 16620
#4 40650
#5 52710
'''

from collections import defaultdict

move = [(0, 0), (0, -1), (1, 0), (0, 1), (-1, 0)]

T = int(input())

for test_case in range(1, T + 1):
    print("#"+str(test_case), end=' ')
    
    graph = defaultdict(list)
    M, A = map(int, input().split())
    
    USER_A, USER_B = [0, ], [0, ]
    USER_A.extend(list(map(int, input().split())))
    USER_B.extend(list(map(int, input().split())))
    
    AP = [0, ]
    for ap in range(1, A + 1):
        X, Y, C, P = map(int, input().split())
        AP. append(P)
        
        for i in range(-C, 1):
            for j in range(-C-i, C+i+1):
                graph[(X+j, Y+i)].append(ap)
                
        for i in range(1, C + 1):
            for j in range(-C+i, C-i+1):
                graph[(X+j, Y+i)].append(ap)

    pt_a, pt_b = (1, 1), (10, 10)
    sum_a, sum_b = 0, 0
    
    for i in range(M + 1):
        pt_a = (pt_a[0] + move[USER_A[i]][0], pt_a[1] + move[USER_A[i]][1])
        pt_b = (pt_b[0] + move[USER_B[i]][0], pt_b[1] + move[USER_B[i]][1])

        m_sum = 0
        m_a, m_b = 0, 0

        if graph[pt_b] and not graph[pt_a]:
            for ap_b in graph[pt_b]:
                if m_b < AP[ap_b]:
                    m_b = AP[ap_b]    
            sum_b += m_b
            continue
            
        elif graph[pt_a] and not graph[pt_b]:
            for ap_a in graph[pt_a]:
                if m_a < AP[ap_a]:
                    m_a = AP[ap_a]
            sum_a += m_a
            continue
        
        for ap_a in graph[pt_a]:
            for ap_b in graph[pt_b]:
                tmp_a, tmp_b = 0, 0
                if ap_a == ap_b:
                    tmp_a = AP[ap_a]//2
                    tmp_b = tmp_a
                else:
                    tmp_a = AP[ap_a]
                    tmp_b = AP[ap_b]
                    
                if m_sum < tmp_a + tmp_b:
                    m_a, m_b = tmp_a, tmp_b
                    m_sum = m_a + m_b
                    
        sum_a += m_a
        sum_b += m_b
        
    print(sum_a + sum_b)