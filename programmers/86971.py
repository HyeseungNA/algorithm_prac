def dfs(now, visited, eum):
  
    for num in eum[now]:
        if visited[num] == 0:
            visited[num] = 1
            dfs(num, visited, eum)

    return 

def solution(n, wires):
    answer = -1
    idx = 0
    while idx < len(wires):
        eum = [[] for _ in range(n + 1)]
        visited = [0] * (n + 1)
        for wire in wires:
            if wire == wires[idx]:
                continue
                
            if wire != wires[idx]:
                eum[wire[0]].append(wire[1])
                eum[wire[1]].append(wire[0])

        print(eum)
        for i in range(1, n + 1):
            if visited[i] == 0 and eum[i] != []:
                visited[i] = 1
                dfs(i, visited, eum)
                print(visited)
                break 
        idx += 1

    return answer


solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])
