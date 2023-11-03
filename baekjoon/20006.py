P, M = map(int,input().split())
rooms = []

# 각각의 플레이어를 입력 받아 방에 넣어주기
for _ in range(P):
    l, n = input().split()
    if not rooms:
        rooms.append([[int(l),n]])
        continue
    
    flag = 1
    for room in rooms:
        if len(room) < M and room[0][0] - 10 <= int(l) <= room[0][0] + 10:
            room.append([int(l),n])
            flag = 0
            break

    
    if flag == 1:
        rooms.append([[int(l),n]])
    
for room in rooms:
    room.sort(key=lambda x:x[1])

for room in rooms:
    if len(room) == M:
        print('Started!')
    else:
        print('Waiting!')
    
    for lv,name in room:
        print(lv,name)



