import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

pre = []
while True:
    try:
        pre.append(int(input()))
    except:
        break


def post(st,ed):
    if st > ed:
        return
    
    mid = ed + 1

    for i in range(st+1,ed+1):
        if pre[i] > pre[st]:
            mid = i
            break
    post(st+1,mid-1)
    post(mid,ed)
    print(pre[st])





post(0,len(pre) - 1)