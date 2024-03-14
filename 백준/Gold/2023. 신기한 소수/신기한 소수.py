
def is_prime(n):
    for i in range(2,int(n/2) + 1):
        if n % i == 0:
            return False
    
    return True

def dfs(num):

    if len(str(num)) == n:
        print(num)
        return
    
    for i in range(10):
        if is_prime(num * 10 + i):
            dfs(num * 10 + i)


n = int(input())


dfs(2)
dfs(3)
dfs(5)
dfs(7)