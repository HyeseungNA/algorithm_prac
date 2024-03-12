from collections import defaultdict, deque
def bfs():
    q = deque()
    q.append([puzzle,0])
    
    while q:
        now_num,cnt = q.popleft()
        now_index = now_num.find('9')

        if now_num == completion:
            return cnt

        y, x = (now_index // 3), (now_index % 3)
        dy = [-1,0,1,0]
        dx = [0,1,0,-1]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < 3 and 0 <= nx < 3:
                next_index = ny * 3 + nx
                next_num = list(now_num)
                next_num[now_index],next_num[next_index] = next_num[next_index], next_num[now_index]
                next_num = ''.join(next_num)

                if next_num not in dic:
                    dic[next_num] += 1
                    q.append([next_num, cnt + 1])


completion = "123456789"
puzzle = ''
for _ in range(3):
    puzzle += ''.join(list(input().split()))
puzzle = puzzle.replace('0','9')
dic = defaultdict(int)
dic[puzzle] = 1
result = bfs()
if result is None:
    print(-1)
else:
    print(result)