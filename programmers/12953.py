# https://programmers.co.kr/learn/courses/30/lessons/12953

def get_div(num, p):
    result = []
    i = 0
    while num > 1:
        if num % p[i] > 0:
            i += 1
        else:
            result.append(p[i])
            num = num // p[i]
    result = set(map(lambda x:(x, result.count(x)), result))
    return result

def solution(arr):
    answer = 1
    prime = []

    # 소수 구하기
    for a in range(2, 100):
        flag = True
        for i in range(2, a):
            if a % i == 0:
                flag = False    
                break
        if flag: prime.append(a)

    # 약수 집합 구하기
    result = set()
    for a in arr:
        result.update(get_div(a, prime))

    result = sorted(list(result), reverse=True)
    visit = set()

    for a in result:
        if a[0] not in visit:
            answer *= (a[0]**a[1])
            visit.add(a[0])

    return answer