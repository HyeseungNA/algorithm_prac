import heapq
import sys


n = int(input())
cards = []
total = 0
for _ in range(n):
    heapq.heappush(cards, int(input()))
while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    tmp = a + b
    total += tmp
    heapq.heappush(cards, tmp)


print(total)
