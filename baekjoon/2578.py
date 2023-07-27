bingo = [list(map(int,input().split())) for _ in range(5)]
numbers = list(map(int,input().split()))

# 2차원 배열을 1차원 배열로 바꿔주기
for _ in range(4):
    numbers += list(map(int,input().split()))
# 색칠
visited = [[0] * 5 for _ in range(5)]


def check():
    answer = 0
    # 가로 확인
    for x in visited:
        if x.count(1) == 5:
            answer += 1
    
    # 세로확인
    for x in range(5):
        bin = 0
        for y in range(5):
            if visited[y][x] == 1:
                bin += 1
        if bin == 5:
            answer += 1

    # 좌상향 대각선 확인
    bin = 0
    for i in range(5):
        if visited[i][i] == 1:
            bin += 1
    
    if bin == 5:
        answer += 1


    # 우상향 대각선 확인
    bin = 0
    for i in range(5):
        if visited[i][4-i] == 1:
            bin += 1
    if bin == 5:
        answer += 1
    
    return answer
# 색칠하기
total = 0
for num in numbers:
    for i in range(5):
        for j in range(5):
            # 불러준 숫자와 빙고판이 같으면
            if bingo[i][j] == num:
                # 색칠해주고
                visited[i][j] = 1
                # 횟수 추가해주기
                total += 1

            # 칠한 개수가 12개 이상이면 check 시작
            if total >= 12:
                # 빙고가 3개면 총 개수 출력하고 
                if check() >= 3:
                    print(total)
                    # 코드 종료
                    exit()
