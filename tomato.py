from collections import deque as dq
queue = dq()

def bfs(queue):
    # 좌표 값이 1인 값을 받아온다
    day = 0 # 토마토 모두가 자라는 일수를 센다
    # 상 하 좌 우 좌표
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while queue:
        x,y = queue.popleft()
        # x, y는 큐에서 꺼낸 좌표 값이다
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue # 만약 이동한 좌표가 맵을 벗어난다면 무시
            if tMap[nx][ny]==0:
                tMap[nx][ny] = tMap[x][y] +1 # 방문처리를 함과 동시에 거리를 이동 거리를 계산한다
                queue.append((nx,ny)) # 큐에 이동된 자표들을 넣는다
            else:
                continue
    if max([tMap[i].count(0) for i in range(n)]):
        return -1
    # elif tMap.count(1) >= 2:
    else:
        for i in range(n):
            for j in range(m):
                day = max(day, tMap[i][j])
        return day-1



m,n = map(int, input().split())
# map 의 크기 m 과 n 을 받아온다
tMap = [list(map(int,input().split())) for i in range(n)] # 토마토 맵을 입력 받는다
for i in range(n):
    for j in range(m):
        if tMap[i][j]==1:
            queue.append((i,j))
day = bfs(queue)
print(day)