from collections import deque as dq


def bfs(x,y):
    queue=dq()
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if nx>=n or ny>=m or nx< 0 or ny<0:
                # 맵을 벗어나면 무시
                continue
            elif ar[nx][ny]==0:
                # 괴물과 조우시 무시
                continue
            elif ar[nx][ny]==1:
                # 큐에 새로운 노드 삽입
                queue.append((nx,ny))
                ar[nx][ny]=ar[x][y]+1 # 이동 거리를 +1 해준다
            else:
                continue
                # 그 외의 경우 모두 무시
    return ar[n-1][m-1] #마지막 출구의 좌표를 찍어준다




n,m = map(int,input().split())
ar=[]
for i in range(n):
    ar.append(list(map(int,input())))
print(bfs(0,0))
print(ar[0][0])