# 가로 가능한 횟수
# 세로 가능한 횟수
# 곱하기
h,w,n,m = map(int,input().split())

w_cnt = ((w - 1) // (m + 1)) + 1
h_cnt = ((h - 1) // (n + 1)) + 1

print(w_cnt * h_cnt)
