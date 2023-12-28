from collections import deque

def solution(priorities, location):
    answer = 0
    cnt = 0
    q = deque()

    for idx, p in enumerate(priorities):
        q.append([idx, p])

    while q:
        idx, p = q.popleft()

        # q 안에서 최댓값을 찾기
        max_priority = max(q, key=lambda x: x[1])[1] if q else p

        if p >= max_priority:
            cnt += 1
            if idx == location:
                answer = cnt
                break
        else:
            q.append([idx, p])

    return answer

# 예시
priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location))
