boards = list(input())

# *개수가 짝수일 때만 확인
now = 0
count = 0
ne = 0
for i in range(len(boards)):
    if boards[i] == 'X':
        ne = i + 1
        count += 1
        # 만약에 카운트가 4개면 A로 채워줄까?
        if count == 4:
            for j in range(now,ne):
                if boards[j] == 'X':
                    boards[j] = 'A'
            now = ne
            count = 0
    elif boards[i] == '.':
        if count % 2 == 0 and count < 4:
            for j in range(now,ne):
                if boards[j] == 'X':
                    boards[j] = 'B'
            now = ne 
            count = 0
        else:
            count = 0
            now = ne 
            continue
if count == 2:
    for j in range(now,ne):
        if boards[j] == 'X':
            boards[j] = 'B'

if 'X' in boards:
    print(-1)
else:
    print(''.join(boards))
            
        