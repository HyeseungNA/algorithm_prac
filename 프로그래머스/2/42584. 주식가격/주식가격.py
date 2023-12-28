from collections import deque
def solution(prices):
    answer = []
    q = deque(prices)
    
    while q:
        price = q.popleft()
        sec = 0
        
        for com in q:
            sec += 1
            if price > com:
                break
        answer.append(sec)
                
    return answer