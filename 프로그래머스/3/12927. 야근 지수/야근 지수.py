from heapq import heappush, heappop
def solution(n, works):
    q = []
    answer = 0
    for work in works:
        heappush(q,(-work,work))
    
    while n > 0:
        w = heappop(q)
        now = w[1]
        now -= 1
        heappush(q,(-now,now))
        n -= 1
    
    for w in q:
        if w[1] >= 0:
            answer += (w[1]) ** 2
    
    return answer

