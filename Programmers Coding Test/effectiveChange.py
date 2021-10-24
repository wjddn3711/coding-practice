n,m = map(int,input().split())
cases = list(int(input()) for _ in range(n))
d = [100001]*(m+1) #0~money 까지
d[0] = 0 # 0원을 만드는 경우 0번을 수행한다
# DP 진행
for i in range(n):
    for j in range(cases[i],m+1):
        if d[j-cases[i]] != 100001: # (i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j],d[j-cases[i]]+1)

if d[m]==100001:
    print(-1)
else:
    print(d[m])
