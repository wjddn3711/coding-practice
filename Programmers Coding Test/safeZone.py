from collections import deque as dq
n = int(input()) # 영역의 크기 설정
zone = [list(map(int,input().split())) for _ in range(n)]

maxVal =0 # 영역내 가장 큰 값을 찾는다
for i in range(n):
    maxVal=max(maxVal,max(zone[i]))

visited = [[list([False]*n) for _ in range(n)] for _ in range(maxVal)]
def safeZ(x,y,k):
    visited[k][x][y]=True # 방문처리
    queue = dq()
    queue.append((x,y))
    # 상하좌우 방향
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while queue:
        x,y = queue.popleft() # 큐에 들어온 순서대로 꺼내준다
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if nx < 0 or ny<0 or nx>=n or ny>=n:
                continue # 좌표를 이탈하는 경우 무시
            else: # 좌표내라면
                if zone[nx][ny] > k and not visited[k][nx][ny]:
                    # 지정한 높이 보다 낮거나 이미 방문한 곳이 아니라면 0으로 바꾼뒤 큐에 삽입
                    visited[k][nx][ny] = True
                    queue.append((nx,ny))

maxCnt = 0
for k in range(maxVal):
    safeCnt =0
    for i in range(n):
        for j in range(n):
            if zone[i][j]>k and not visited[k][i][j]:
                safeZ(i,j,k)
                safeCnt+=1
        maxCnt = max(maxCnt,safeCnt)
print(maxCnt)


