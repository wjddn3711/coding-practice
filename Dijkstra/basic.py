v,e = map(int, input().split()) # v = 정점의 개수, e = 간선의 개수
start = int(input()) # k = 시작 정점의 번호

INF = int(1e6) # 무한대를 나타내줄 수
dist = [INF]*(v+1) # 거리를 처음에 무한대로 모두 초기화 해준다
visited = [False]*(v+1) # 방문여부를 체크하는 목적의 리스트
graph = [[] for _ in range(v+1)] # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트

for _ in range(e):
    a,b,c = map(int, input().split())
    # a 노드에서 b 노드까지 가는 비용이 c 이다
    graph[a].append((b,c))
    #[[], [(2, 2), (3, 3)], [(3, 4), (4, 5)], [(4, 6)], [], [(1, 1)]] 최종 결과


def getShortDist():
    minValue = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1,v+1):
        if dist[i]<minValue and not visited[i]:
            minValue=dist[i]
            index = i
    return index


def dijistra(start):
    dist[start] = 0  # 시작노드에서 자기 자신까지의 거리는 0이다
    visited[start] = True  # 시작노드를 방문처리시킨다
    for i in graph[start]: # 시작 노드와 연결된 다른 노드들의 거리값을 dist에 담아준다
        dist[i[0]] = i[1]
    for i in range(v-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문처리
        now = getShortDist()
        visited[now] = True # 해당노드로 이동후 방문처리
        for j in graph[now]: # 현재 노드에서 갈 수 있는 노드동안 반복
            cost = dist[now]+j[1] # j[1]에는 해당 노드까지 가는 비용이 저장되어있다
            if cost < dist[j[0]]: # j[0]에는 해당 노드가 담겨있고 만약 비용이 현재 거리보다 작다면 그 거리로 초기화해준다
                dist[j[0]] = cost

dijistra(start) # 시작노드를 기준으로 다익스트라 실행

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1,v+1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if dist[i] == INF:
        print('INF')
    # 도달할 수 있는 경우, 거리를 출력
    else:
        print(dist[i])
