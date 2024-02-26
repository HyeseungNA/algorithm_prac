
n,d,k,c = map(int,input().split())
sushi = []
for _ in range(n):
    sushi.append(int(input()))
sushi = sushi + sushi[0:n-1]

idx = 0
Max_length = 0
while idx <= len(sushi) - k:
    result = sushi[idx:idx+k]
    result.append(c)
    Max_length = max(Max_length, len(set(result)))
    idx += 1

print(Max_length)