import sys

input = sys.stdin.readline
n = int(input())
result = []

for _ in range(n):
    word1, word2 = input().split()
    result.append(word2.upper()[word1.upper().find('X')])

print(''.join(result))
