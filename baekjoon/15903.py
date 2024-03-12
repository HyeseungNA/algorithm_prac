import heapq
n,m = map(int,input().split())
cards = list(map(int,input().split()))

heapq.heapify(cards)
cnt = 0
while cnt < m:
    num1 = heapq.heappop(cards)
    num2 = heapq.heappop(cards)

    total = num1 + num2
    heapq.heappush(cards,total)
    heapq.heappush(cards,total)
    cnt += 1

print(sum(cards))