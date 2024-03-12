import itertools
n = int(input())
ability = [list(map(int,input().split())) for _ in range(n)]
people = [i for i in range(1,n+1)]

starks = list(itertools.combinations(people,len(people)//2))

Min = int(1e9)

for stark in starks: # 스타크가 꾸릴 수 있는 사람들
    link = []
    
    for p in people:
        if p not in stark:
            link.append(p) # 링크 팀이 꾸릴 수 있는 사람들

    s = list(itertools.combinations(stark,2))
    l = list(itertools.combinations(link,2))
    s_score = 0
    l_score = 0
    for i, j in s:
        s_score += ability[i-1][j-1] + ability[j-1][i-1]
    
    for ii, jj in l:
        l_score += ability[ii-1][jj-1] + ability[jj-1][ii-1]

    Min = min(Min,abs(s_score-l_score))

    

print(Min)
    