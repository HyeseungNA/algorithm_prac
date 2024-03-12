import heapq,sys
input = sys.stdin.readline
n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(heap,(-num,num))
    else:
        if not heap:
            print(0)
        else:
            result = heapq.heappop(heap)[1]
            print(result)