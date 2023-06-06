def solution(tickets):
    def dfs(name):
        nonlocal answer,tmp
        tmp = {}
        for depart in range(len(tickets)):
            for arrive in range(len(tickets)):
                # 같은 출발지이고, 방문을 안하고, 다음 경로로 이동할 수 있을때 
                if tickets[depart][0] == name and visited[depart][1] == 0 and tickets[depart][1] == tickets[arrive][0] and visited[arrive][1] == 0:
                    # 딕셔너리에 넣는과정
                    tmp[depart] = tickets[depart][1]
        print(tmp)
        # tmp 정렬해서 맨 처음값 뽑아내기
        if len(tmp) >= 1:
            dic = sorted(tmp.items(),key = lambda x:x[1])
            # 방문처리하고
            next_y = dic[0][0]
            next_name = dic[0][1]
            visited[next_y][1] = 1

            # 결과값에 공항 이름 넣고
            answer.append(next_name)
            print(next_name)
            #dfs돌아
            dfs(next_name)

              
    answer = ['ICN']
    tmp = []
    visited = [[0]* 2 for _ in range(len(tickets))]
    # 인천에서 출발!
    for i in range(len(tickets)):
        if tickets[i][0] == 'ICN':
            visited[i][0] = 1
            dfs(tickets[i][0])
            break
        
    # 남은 공항 추가
    for i in range(len(tickets)):
        if visited[i][1] == 0:
            answer.append(tickets[i][1])

    return answer