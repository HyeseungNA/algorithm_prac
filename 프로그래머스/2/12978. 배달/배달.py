import heapq
def solution(N, road, K):
    INF = 1e9
    graph = [[] for _ in range(N+1)]
    distance = [INF] * (N+1)
    answer = 0
    q = []
    for r in road:
        st, ed, time = r[0], r[1], r[2]
        graph[st].append((ed, time))  # 도착 지점, 시간
        graph[ed].append((st,time))
    
    distance[1] = 0
    heapq.heappush(q,[0,1])
    
    while q:
        dist,now = heapq.heappop(q) # 거리,출발점
        

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    for d in distance:
        if d <= K:
            answer += 1
    return answer


