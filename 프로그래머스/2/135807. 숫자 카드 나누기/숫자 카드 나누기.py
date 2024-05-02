import math
def solution(arrayA, arrayB):
    answer = 0
    n = len(arrayA)
    
    # A배열 최대 공약수 구하기
    a = arrayA[0]
    b = arrayB[0]

    for i in range(1,n):
        a = math.gcd(a,arrayA[i])
        b = math.gcd(b,arrayB[i])
    
       
    
    # 초기 상태
    checkA = 1
    checkB = 1
    
    # 둘 다 나눠진다면
    for i in range(n):
        if arrayA[i] % b == 0:
            checkA = 0
        if arrayB[i] % a == 0:
            checkB = 0
    
    if checkA == 0 and checkB == 0:
        return 0
    
    else:
        answer = max(a,b)
    return answer