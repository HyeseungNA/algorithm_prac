def solution(arr):
    result=[0,0]
    length=len(arr)
    
    def compression(a,b,l):
        start=arr[a][b]
        for i in range(a,a+l):
            for j in range(b,b+l):
                if arr[i][j]!=start: # 같지 않으면 더 깊게 압축
                    l=l//2
                    compression(a,b,l)
                    compression(a,b+l,l)
                    compression(a+l,b,l)
                    compression(a+l,b+l,l)
                    return
                
        result[start]+=1
        
    compression(0,0,length)
    
    return (result)
solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])