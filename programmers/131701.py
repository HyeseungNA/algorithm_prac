# dfs로 풀기

def dfs(idx,n,tmp,cnt,elements,visited,lst):
    n_idx = 0

    # 방문처리해주기
    visited[idx] = 1
    tmp.append(elements[idx])
    


    # n과 같으면 tmp를 lst안에 넣고 비워주기
    if cnt == n:
        # lst에 넣기
        lst.append(sum(tmp))
        return 

    for i in range(len(elements)):

        # 절대값이 1일 때
        if abs(abs(idx) - abs(i)) == 1 or (idx == 0 and i == len(elements)-1) or (idx == len(elements)-1 and i == 0):
            n_idx = i
            if visited[n_idx] == 0:
                visited[n_idx] = 1
                dfs(n_idx,n,tmp,cnt+1,elements,visited,lst)
                visited[n_idx] = 0
                if tmp:
                    tmp.pop()

    
def solution(elements):
    # 결과 리스트
    lst = []
    # 임시 리스트

    for i in range(1,len(elements) + 1):
        print(lst)
        # 방문처리
        visited = [0] * (len(elements) + 1)
        for idx in range(len(elements)): 
            tmp = []
            # 방문을 안하면 dfs 시작
            if visited[idx] == 0:
                dfs(idx,i,tmp,1,elements,visited,lst)
    return len(set(lst))

answer = solution([7,9,1,1,4])
print(answer)