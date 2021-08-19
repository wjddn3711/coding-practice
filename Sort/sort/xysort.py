n = int(input())
ar = [list(map(int,input().split())) for _ in range(n)]
ar.sort(key= lambda x:(x[0],x[1]))
[print(ar[i][0],ar[i][1]) for i in range(n)]