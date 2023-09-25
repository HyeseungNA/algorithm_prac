# pipe 개수
# piece 개수


order = list(input())

pipe = 0
piece = 0

for i in range(len(order)):
    if order[i] == '(':
        pipe += 1
    
    elif order[i] == ')':
        # 만약에 전에 '('이었으면 pipe 개수 줄여주고 pipe 개수만큼 조각 추가
        if order[i-1] == '(':
            pipe -=1
            piece += pipe

        # 만약에 전에 ')'이었으면 pip개수 줄여주고 조각 한개 추가
        if order[i-1] == ')':
            pipe -= 1
            piece += 1

print(piece)