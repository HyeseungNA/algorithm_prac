def sqare(k):
    global lst
    for y in range(5):
        for x in range(5):
            if lst[y][x] == '' and used[ord(k) - 65] == 0:
                used[ord(k) - 65] = 1
                lst[y][x] = k
                return
    return
            
# 배열에 채워넣기
lst = [[''] * 5 for _ in range(5)]
message = list(input())

key = list(input())

# 사용했는지 여부확인
used = [0] * 26

# key 사용을 안했으면 배열에 넣어주기
for k in key:
    sqare(k)
'''
HELLOWORLD
PLAYFAIRCIPHERKEY

'''
# 나머지도 넣어주기
for i in range(26):
    if i != 9:
        sqare(chr(i+65))

# 메시지를 두 글자씩 나누기
idx = 0
words = []
answer = ''
word1 = ''
word2 = ''
while idx < len(message):
    
    # 나머지가 0일 때
    if idx % 2 == 0:
        word1 = message[idx]
    # 나머지가 1일때
    elif idx % 2 == 1:
        word2 = message[idx]
    
    # 두 문자가 같은지 비교
    if word1 == word2:
        # 두 문자가 x일 때
        if word1 == 'X':
            word2 = 'Q'
        # 그 외에는 중간에 X 넣어주기
        else:
            word2 = 'X'


    else:
        idx += 1
    
    # 마지막 인덱스이고 나머지가 없으면 뒤에 x를 붙여주기
    if idx == len(message) - 1 and idx % 2 == 0:
        answer += word1
        answer += 'X'
    else:

        answer += word1
        answer += word2
    if word1 != '' and word2 != '':
        words.append(answer)
        answer = ''
        word1 = ''
        word2 = ''

print(words)



# 쌍들을 돌면서

# 1. 같은 행에 있는지

# 2. 같은 열에 있는지

# 3. 그 외