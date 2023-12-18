import heapq

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))

    while q:
        time,x = heapq.heappop(q)
        if distance[x] < time:
            continue

        for a,b in [(x-1,time + 1), (x + 1, time + 1) , (2 * x, time)]:
            if 0 <= a <= 100000 and distance[a] > b:
                distance[a] = b
                heapq.heappush(q,(b,a))

n, k = map(int,input().split())
INF = int(1e9)
distance = [INF] * (100001)

dijkstra(n)

print(distance[k])