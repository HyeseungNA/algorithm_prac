def solution(n, s, a, b, fares):
    INF = 10000000
    answer = INF
    graph = [[INF] * (n+1) for _ in range(n+1)]
    
    for i in range(n+1):
        for j in range(n+1):
            if i == j:
                graph[i][j] = 0
    
    for fare in fares:
        node1,node2,fee = fare
        graph[node1][node2] = fee
        graph[node2][node1] = fee
        
    
    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
    
    for t in range(n+1):
        tmp = graph[s][t] + graph[t][a] + graph[t][b]
        answer = min(tmp,answer)
    

    return answer