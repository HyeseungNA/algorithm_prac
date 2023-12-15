def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if b in truth:
        parent[a] = b
    elif a in truth:
        parent[b] = a
    else:
        if a < b:
            parent[b] = a
        elif a > b:
            parent[a] = b

n, m = map(int, input().split())
truth = set(map(int, input().split()[1:]))  # set으로 변경하고 첫 번째 원소 제외
parties = []
parent = list(range(n + 1))
ans = 0

for _ in range(m):
    party_info = list(map(int, input().split()))
    party_len = party_info[0]
    party = party_info[1:]

    for i in range(party_len - 1):
        union(parent, party[i], party[i + 1])

    parties.append(party)

ans = 0
for party in parties:
    for i in range(len(party)):
        if find(parent, party[i]) in truth:
            break
    else:
        ans += 1

print(ans)
