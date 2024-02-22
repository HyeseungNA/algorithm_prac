n,m = map(int,input().split())
lst1 = list(map(int,input().split()))
lst2 = list(map(int,input().split()))
lst3 = lst1[::] + lst2[::]

lst3.sort()
print(*lst3)