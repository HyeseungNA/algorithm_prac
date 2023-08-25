# 모음 리스트에 넣기
# 모음/자음 갯수 조합하기
# dfs 돌리면서 개수 찾기
def dfs1(st,cnt,dept,lst):
    global total1

    # 현재 깊이가 cnt와 같으면 그만
    if cnt == dept:
        total1 += 1
        return 

    for i in range(st+1,len(vowel)):
        lst.append(vowel[i])
        dfs1(i,cnt, dept + 1,lst)

def dfs2(st,cnt,dept,lst2):
    global total2

    # 현재 깊이가 cnt와 같으면 그만
    if cnt == dept:
        print(lst2)
        total2 += 1
        return 

    for i in range(st+1,len(consonant)):
        lst2.append(consonant[i])
        dfs2(i,cnt, dept + 1,lst2)
        lst2.pop()


n,m = map(int,input().split())
chars = list(input().split())

lst = ['a','e','i','o','u']

vowel = []
consonant = []

answer = []
for c in chars:
    if c in lst:
        vowel.append(c)
    else:
        consonant.append(c)

for i in range(1,len(vowel) + 1):
    for j in range(2,len(consonant) + 1):
        # 모음, 자음 숫자 조합
        if i + j == n:
            # print(i,j,'🌸')
            lst = []
            lst2 = []
            for m in range(len(vowel)): 
                total1 = 0 # 모음 조합 가능 갯수
                total2 = 0 # 자음 조합 가능 갯수
                lst = [vowel[m]] # 모음 넣는 리스트
                dfs1(m,i,1,lst)
                # print(total1,'🌹')
               
                for k in range(len(consonant)):
                    lst2.append(consonant[k])
                    dfs2(k,j,1,lst2)
                    lst2.pop()
                # print(total2,'___') 
                # print(total1,'🫢')
                # print(answer,'❗️')
            
           
