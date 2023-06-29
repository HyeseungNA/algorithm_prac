def solution(n):
    answer = 0
    start = 1
    idx = 0
    total = start
    # start가 n이 될 때까지 반복
    while start <= n:
        
    # idx를 하나씩 더해준다. 
        if total < n:
            idx += 1
            end = start + idx
            total += end
    
        if total == n:
            answer += 1
            start += 1
            idx = 0
            total = start
        if total > n:
            idx = 0
            start += 1
            total = start
        
    # 총합이 n이랑 같으면 cnt 더해준다.
    return answer

