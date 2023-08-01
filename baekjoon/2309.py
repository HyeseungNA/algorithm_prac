# cnt가 7명이면 난쟁이 총 키 합을 구해야한다.


def find_dwarf(start, cnt,total):
    global result 
    if cnt == 7:
        # 키 총합이 100이면 난쟁이들을 출력해주세요
        if total == 100:
            return result
        return
    
    for index in range(start, 9):
        # result에 난쟁이들을 넣어주세요
        result.append(dwarf[index])
        # 키 총합에 난쟁이 키 더해주세요
        find_dwarf(index+1, cnt+1, total+ dwarf[index])
        
         # result 합이 100이면 for문을 멈춰주세요
        if sum(result) == 100:
            break
        result.pop()



dwarf = list(int(input()) for _ in range(9))
print(dwarf)
# 오름차순으로 정렬부터
dwarf.sort()


# 난쟁이 들어가는 리스트
result = []
# 시작하는 인덱스, 난쟁이 수, 키 총합
find_dwarf(0, 0, 0)
