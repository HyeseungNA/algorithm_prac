from collections import deque

def solution(order):
    stack = []
    n = len(order)
    order = deque(order)
    answer = 0
    i = 1

    while i <= n:
        # print(i, stack)
        stack.append(i)
        
        while order and stack:
            if order[0] == stack[-1]:
                answer += 1
                # print(order[0], stack)
                stack.pop()
                order.popleft()
            else:
                break
        i += 1

    return answer
