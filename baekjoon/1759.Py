# n 만큼 조합으로 만들기
# n만큼 채워졌으면, 모음 자음 확인하기
# 맞으면 출력해여

def check():
    vcnt = 0
    ccnt = 0

    for c in lst:
        if c in vowels:
            vcnt += 1
        else:
            ccnt += 1
    
    if vcnt >= 1 and ccnt >= 2:
        return True


def dfs(now,cnt):
    if cnt == n:
        if check():
            print("".join(lst))
        return

    for i in range(now,m):
        # 암호넣기
        lst.append(keys[i])
        dfs(i+1,cnt+1)
        lst.pop()


n,m = map(int,input().split())
keys = list(input().split())
keys.sort()
vowels = ['a','e','i','o','u']
lst = [] # 암호 넣기
dfs(0,0) # 처음 시작, 깊이
