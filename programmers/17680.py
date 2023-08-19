from collections import deque
def solution(cacheSize, cities):
    answer = 0
    q = deque(maxlen=cacheSize)
    if cacheSize == 0:
        answer = 5 * len(cities)
    else:
        for i in range(len(cities)):
            # q안에 이미 있으면 빼주기
            if cities[i].lower() in q:
                q.remove(cities[i].lower())
                q.append(cities[i].lower())
                answer += 1
                continue
            else:
                q.append(cities[i].lower())
                answer += 5
    print(answer)
    return answer
solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])