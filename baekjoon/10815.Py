def binary_search(target):
    st = 0
    ed = len(cards) - 1

    while st <= ed:
        mid = (st + ed) // 2

        if cards[mid] == target:
            return 1
        
        elif cards[mid] < target:
            st = mid + 1
        
        else:
            ed = mid - 1
    return 0


n = int(input())
cards = list(map(int,input().split()))

m = int(input())
numbers = list(map(int,input().split()))
cards.sort() # nlogn
result =[]
for number in numbers:
    result.append(binary_search(number)) # mlogn

print(*result)