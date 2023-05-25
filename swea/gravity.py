testcase = int(input())
for tc in range(testcase):
    n = int(input())
    list = list(map(int, input().split()))
    # 리스트 요소보다 크거나 같은 갯수 구하기
    result = []
    for i in range(n-1):
        cnt = 1
        for j in range(n):
            if list[i] <= list[j]:
                cnt += 1
            print(cnt)
            result.append(n - cnt)
    
    print(f'#{tc+1} {max(result)}')
            

'''
1
9
7 4 2 0 0 6 0 7 0
'''

