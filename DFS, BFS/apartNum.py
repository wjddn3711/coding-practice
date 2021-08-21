from collections import deque as dq
def bfs(x,y):
    house = 1
    ar[x][y]=0 # 받은 위치는 0으로 초기화
    # 상 하 좌 우 이동시 좌표
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = dq()
    queue.append((x,y)) # x, y 좌표를 큐에 담는다
    while queue: # 더이상 인접하는 좌표가 없을 때 까지
        x, y = queue.popleft()
        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue # 좌표가 맵을 벗어난다면 무시
            elif ar[nx][ny]!=1:
                continue # 좌표가 집이 없는 곳이라면 무시
            elif ar[nx][ny]==1:
                house+=1 # 집 +1
                ar[nx][ny] =0 # 방문처리
                queue.append((nx,ny))
            else:
                continue
    return house


# 입력 받을 열의 수를 받는다
n = int(input())
ar = [list(map(int,input())) for _ in range(n)]
hCnt = [] # 아파트 동의 개수를 담을 리스트
for i in range(n):
    for j in range(n):
        if ar[i][j]==1: # (0,0)~(n-1,n-1)까지 집이 있는 경우 bfs를 수행한다
            x = bfs(i,j)
            hCnt.append(x)
hCnt.sort() # 집의 개수를 오름차순으로 바꿔준다
print(len(hCnt)) # 동의 개수
[print(i) for i in hCnt] # 집의 개수