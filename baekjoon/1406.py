st_L = list(input())
st_R = []
m = int(input())
for _ in range(m):
    order = list(input().split())
    if order[0] == 'L' and st_L:
        st_R.append(st_L.pop(-1))
    elif order[0] == 'P':
        st_L.append(order[1])
    elif order[0] == 'D' and st_R:
        st_L.append(st_R.pop(-1))
    elif order[0] == 'B' and st_L:
        st_L.pop(-1)
answer = st_L + st_R[::-1]
print(''.join(answer))