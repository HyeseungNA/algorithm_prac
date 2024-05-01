import heapq
def solution(operations):
    answer = []
    q = []
    
    for operation in operations:
        order,num = operation.split(' ')
        if order == 'I':
            heapq.heappush(q,int(num))
        
        else:
            if q:
                if int(num) == -1:
                    num = heapq.heappop(q)
                else:
                    q.remove(max(q))
    
    if not q:
        answer = [0,0]
    else:
        answer = [max(q),heapq.heappop(q)]

            
            
    return answer