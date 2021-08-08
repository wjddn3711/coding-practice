def dfs(x,y):
    if x<=-1 or y<=-1 or x>=n or y>=m:
        return False
    elif ar[x][y]==0:
        ar[x][y]=1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    else:
        return False




n,m = map(int,input().split())
ar = list()
for i in range(n):
    ar.append(list(map(int,input())))

cnt=0
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            cnt+=1

print(cnt)