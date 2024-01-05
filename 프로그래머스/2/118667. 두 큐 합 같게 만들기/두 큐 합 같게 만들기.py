from collections import deque
def solution(queue1, queue2):
    n = len(queue1 + queue1) * 2
    q1 = deque(queue1)
    q2 = deque(queue2)
    cnt = 0
    total1 = sum(q1)
    total2 = sum(q2)
    answer = -2
    Min = int(1e9)
    
    
    while cnt <= n:
#         print(q1)
#         print(q2)
#         print(cnt, sum(q1),sum(q2))
        
        if total1 == total2:
            if Min > cnt:
                Min = cnt
            break
        
        if total1 < total2:
            out = q2.popleft()
            q1.append(out)
            total1 += out
            total2 -= out
            cnt += 1
            continue
        
        elif total2 < total1:
            out = q1.popleft()
            q2.append(out)
            total2 += out
            total1 -= out
            cnt += 1
            continue
            
    if Min == int(1e9):
        answer = -1
    else:
        answer = Min
    return answer

