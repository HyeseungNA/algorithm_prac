from collections import deque
def solution(queue1, queue2):
    n = len(queue1 + queue1)
    q1 = deque(queue1)
    q2 = deque(queue2)
    cnt = 0
    total = (sum(queue1) + sum(queue2)) // 2
    print(total)
    answer = -2
    Min = int(1e9)
    
    
    while cnt <= n:
        
        if sum(q1) == total and sum(q2) == total:
            if Min > cnt:
                Min = cnt
            break
        
        if sum(q1) < total:
            out = q2.popleft()
            q1.append(out)
            cnt += 1
            continue
        
        elif sum(q2) < total:
            out = q1.popleft()
            q2.append(out)
            cnt += 1
            continue
        
        elif sum(q1) > total:
            out = q1.popleft()
            q2.append(out)
            cnt += 1
            continue
            
        elif sum(q2) > total:
            out = q2.popleft()
            q1.append(out)
            cnt += 1
            continue
    
    print(Min)
    return answer
solution([3, 2, 7, 2],[4, 6, 5, 1])
