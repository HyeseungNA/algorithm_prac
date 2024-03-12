n = int(input())
scores = []

for _ in range(n):
    scores.append(int(input()))

scores = scores[::-1]
now = scores[0] - 1
cnt = 0
for score in scores[1:]:
    if score > now:
        cnt += (score - now)
        now -= 1
    
    else:
        now = score - 1
print(cnt)
