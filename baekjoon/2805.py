N, M = map(int, input().split())
trees = list(map(int, input().split()))
st, ed = 1, max(trees) #이분탐색 검색 범위 설정

while st <= ed:
    mid = (st + ed) // 2

    result = 0
    for tree in trees:
        if tree >= mid:
            result += tree - mid
    
    if result >= M:
        st = mid + 1
    else:
        ed = mid - 1

print(ed)