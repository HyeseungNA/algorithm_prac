arr =  [[0,0,1,0,0],
        [0,1,0,0,0],
        [1,0,0,2,1],
        [0,0,0,1,0],
        [0,0,0,0,0]]

change = 0
while True:
    dy = [-1,0,1,0]
    dx = [0,-1,0,1]

    for i in range(4):
        for j in range(5):

            if arr[i][j] == 1:
                y = i
                x = j
                flag = 0
                # print(y,x,flag,'🤪')
                
            
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    # print(ny,nx,'🧐')
                    if 0 <= ny <= 4 and 0 <= nx <= 4 and arr[ny][nx] == 2:
                        # print(y,x,ny,nx,'🌹')
                        flag = 1

                # print(y,x,flag,'🌸')
                if flag == 0 and arr[y+1][x] == 0:
                    print(y+1,x,y,x)
                    arr[y+1][x], arr[y][x] = arr[y][x] , arr[y+1][x]
                    change = 1
                    # print(arr)
    
    else:
        change = 0
    
    if change == 0:
        break
     
print(arr)

    
