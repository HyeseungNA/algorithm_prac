import heapq
def solution(n, k, enemy):
    q = []
    
    for i, ele in enumerate(enemy):
        heapq.heappush(q,ele)
        if len(q) > k:
            n -= heapq.heappop(q)
        if n < 0:
            return i
    
    return len(enemy)
   