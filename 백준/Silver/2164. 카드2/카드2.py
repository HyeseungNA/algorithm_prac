from collections import deque
n = int(input())
cards = deque([i for i in range(1,n+1)])

while len(cards) > 1:
    num1 = cards.popleft()
    num2 = cards.popleft()
    cards.append(num2)

print(cards[-1])