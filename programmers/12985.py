def solution(n,a,b):
    # 둘이 만날 때까지 반복
    cnt = 0
    while True:
        if a == b:
            break
        a = (a//2) + (a % 2)
        b = (b//2) + (b % 2)
        cnt += 1
            
    return cnt   
