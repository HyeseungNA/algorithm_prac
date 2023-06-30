def solution(n):
    answer = 0
    
    a = [0] * 1000000
    a[0] = 0
    a[1] = 1 
    for i in range(2,n+1):
        a[i] = a[i-2] + a[i-1]
    
    answer = a[n]


    return answer

