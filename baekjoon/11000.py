import heapq

n = int(input())
rooms = []
for _ in range(n):
    s,t = map(int,input().split())
    rooms.append([s,t])
rooms.sort(key=lambda x:(x[0],x[1]))

heap = [rooms[0][1]]

for i in range(1,n):
    if rooms[i][0] >= heap[0]:
        heapq.heappop(heap)
    heapq.heappush(heap,rooms[i][1])
    
print(len(heap))