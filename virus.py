from collections import deque as dq
def bfs(virusMap, v):
    queue = dq([v]) # 바이러스가 걸린 컴퓨터를 시작으로 큐에 담아준다
    while queue:
        x = queue.popleft()
        for i in range(len(virusMap)):
            # 바이러스 맵의 길이 만큼 반복한다
            if virusMap[i][x]==1 and i not in visited and i not in queue:
            # 만약 연결된 컴퓨터이고 방문하지 않은 컴퓨터이며 비교대상의 컴퓨터가 자기 자신이 아닐때
                visited.append(i) # 방문처리를 한다
                queue.append(i) # 큐에도 담아준다
    # print(visited)
    return len(visited)-1


n = int(input()) # 컴퓨터의 수
link = int(input()) # 연결된 링크 수

virusMap = [[0 for _ in range(n+1)] for _ in range(n+1)]
# 컴퓨터가 연결된 자표를 저장할 바이러스맵을 0으로 초기화한다

for _ in range(link):
    x, y = map(int, input().split()) #연결된 컴퓨터를 입력받는다
    virusMap[x][y]=1 # 0으로 초기화된 맵에서 연결된 컴퓨터는 1로 표기한다
    virusMap[y][x]=1 # x,y 뿐만 아니라 y,x 또한 연결되있다 처리한다

v=1 # 바이러스가 걸린 컴퓨터
visited = [v]
print(bfs(virusMap,v))