import sys
sys.setrecursionlimit(10**6) # 재귀제한 풀어주기
def dfs1(first,towork):
    global start,end

    # 이동한 지점이 출발지이거나 도착지이면 return을 해줘라
    if first == end:
        return towork
    
    # 출발지에서 갈 수 있는 지점들 돌면서 이동하기
    for point in lines[first]:
        # 방문을 하지 않았다면
        if visited[point] == 0:
            # print(point)
            # 방문처리해주기
            visited[point] = 1
            # 방문 횟수 더해주기
            tohome[point] += 1
            # print(visited)
            dfs1(point,cnt + 1,towork)
            # 다시 방문 풀어주기
            visited[point] = 0
    return

def dfs2(first,tohome):
    global start,end

    # 이동한 지점이 출발지이거나 도착지이면 return을 해줘라
    if first == start:
        return tohome
    
    # 출발지에서 갈 수 있는 지점들 돌면서 이동하기
    for point in lines[first]:
        # 방문을 하지 않았다면
        if visited[point] == 0:
            # print(point)
            # 방문처리해주기
            visited[point] = 1
            # 방문 횟수 더해주기
            tohome[point] += 1
            # print(visited)
            dfs2(point,cnt + 1,tohome)
            # 다시 방문 풀어주기
            visited[point] = 0
    return 
n,m = map(int,input().split())
lines = [[] for _ in range(n+1)] # 경로를 담음
count = [0] * (n + 1) # 방문 횟수
visited = [0] * (n + 1) # 방문처리해줌
for _ in range(m):
    first,second = map(int,input().split())
    lines[first].append(second)
start,end = map(int,input().split())

visited[start] = 1 # 방문 처리 해주기
visited[end] = 1 # 방문 처리 해주기
towork = [0] * (n + 1)
tohome = [0] * (n + 1)
towork[start] += 1
tohome[end] += 1
dfs1(start,towork)
dfs2(end,tohome)

answer = 0
for i in range(n+1):
    # 시작점과 도착점이 아닌 지점들 중에서
    if i != start and i != end:
        if tohome and towork:
            answer += 1
        

print(answer)
''' 
5 9
1 2
1 4
2 1
2 3
3 4
3 5
4 1
4 3
5 1
1 3

'''