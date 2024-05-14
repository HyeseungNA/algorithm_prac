import heapq
def solution(A, B):
    cnt = 0
    A.sort()
    heapq.heapify(B)
    i = 0
    while B:
        b = heapq.heappop(B)
        if A[i] < b:
            i += 1
            cnt += 1
    
    

    return cnt