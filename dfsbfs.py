from collections import deque as dq
def dfs(ar,v,visited):
    visited[v]=True
    print(v, end=' ')
    for item in ar[v]:
        if not visited[item]:
            dfs(ar,item,visited)

def bfs(ar,v,visited):
    print()
    queue = dq([v])
    # queue.append(v)
    visited[v]=True
    while queue:
        v1=queue.popleft()
        print(v1, end=' ')
        for item in ar[v1]:
            if not visited[item]:
                queue.append(item)
                visited[item]=True


n,m,v = map(int,input().split())
ar=[]
for i in range(m):
    ar.append(list(map(int,input().split())))
visited = [False]*m

dfs(ar,v,visited)
bfs(ar,v,visited)