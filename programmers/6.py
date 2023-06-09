def solution(tickets):
    
    answer = []
    visited = [0] * len(tickets)
    
    def dfs(airport, path):
        # 티켓 다 쓰면
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return
        
        for idx, ticket in enumerate(tickets):
            # 방문 안하고 도착지가 다음 출발지랑 같을 때
            if visited[idx] == 0 and airport == ticket[0]:
                visited[idx] = 1
                dfs(ticket[1], path + [ticket[1]])
                visited[idx] = 0
    
    dfs('ICN',["ICN"])
    
    answer.sort()
    return answer[0]
        
        
        
        