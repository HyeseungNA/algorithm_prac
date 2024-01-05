def comp(x,y,n,arr):
    global answer
    init = arr[y][x]
    for i in range(y, y + n):
        for j in range(x, x + n):
            if arr[i][j] != init:
                nn = n // 2
                comp(x,y,nn,arr)
                comp(x+nn,y,nn,arr)
                comp(x,y+nn,nn,arr)
                comp(x+nn,y+nn,nn,arr)
                return
    
    
    answer[init] += 1
answer = [0,0] 
def solution(arr):
    global answer
    n = len(arr)  
    comp(0,0,n,arr)
    return answer