from collections import deque

def solution(bridge_length, weight, truck_weights):
    waiting = deque(truck_weights)
    bridge = deque([0] * (bridge_length))
    time = 0
    total = 0
    while bridge:
        total -= bridge.popleft()
        time += 1
        if waiting:
            if total + waiting[0] <= weight:
                w = waiting.popleft()
                bridge.append(w)
                total += w
            else:
                bridge.append(0)

    return time
