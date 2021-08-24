INF = int(1e6) # 무한을 의미하는 큰수 생성

# 노드의 개수 및 간선의 개수 입력받기
n,m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)] # 2차원 리스트를 만들고, 모든값을 무한대로 초기화

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b: # 만약 자기 자신이라면
            graph[a][b]=0 # 0으로 초기화

# 각 간선에 대한 정보를 입력받아 그값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a,b,c = map(int, input().split())
    graph[a][b]=c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

# 수행된 결과 출력
for a in range(1,n+1):
    for b in range(1,n+1):
        # 도달할 수 없는 경우, 무한이라고 출력
        if graph[a][b]==INF:
            print('INF')
        else:
            print(graph[a][b])


