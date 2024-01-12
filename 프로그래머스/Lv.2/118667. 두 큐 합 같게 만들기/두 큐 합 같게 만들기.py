from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    answer = 0
    total = sum(q1 + q2) // 2
    total2 = sum(q1)
    cnt = 0
    n = len(queue1) * 4
    while True:
        
        if cnt >= n:
            answer = -1
            break
        
        if total2 > total:
            now = q1.popleft()
            total2 -= now
            q2.append(now)
            cnt += 1
        if total2 < total:
            now = q2.popleft()
            total2+= now
            q1.append(now)
            cnt += 1
        if total2 == total:
            answer = cnt
            break
            
    return answer

