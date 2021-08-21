import heapq
import sys
input = sys.stdin.readline
v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v+1)] # 각 노드와 연결된 노드들을 입력받을 리스트
INF = int(1e6) # 임의로 무한대를 설정해준다
distance = [INF] * (v+1) # 초기 거리를 무한대로 하고 노드의 개수 만큼 생성해준다
# v+1 을 하는 이유는 리스트가 0 부터 시작하기에 매번 해당 노드를 호출할때 -1을 하는 번거로움을 덜기 위해 0번째 인덱스를 무한대로 더 만들어준다
for _ in range(e):
    a, b, dis = map(int, input().split()) # a=기준노드, b=기준노드와 연결된 노드, c = a와b 사이 거리
    graph[a].append((b,dis))

def dijikstra(k):
    queue = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    distance[k] = 0 # 시작노드 부터 자기 자신까지의 거리는 0으로 설정
    heapq.heappush(queue,(0, k)) # 초기 q = [(0, k)]
    while queue: # 큐가 빌때 까지 반복
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(queue)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for num in graph[now]:
            cost = num[1] + dist # 현재 거리 + 이동할 거리
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[num[0]]:
                distance[num[0]]=cost
                heapq.heappush(queue,(cost,num[0]))
dijikstra(k) # 다익스트라 알고리즘 수행

for i in range(1, v+1):#distance[0]에는 INF가 들어있으며 garbage 값이다
    if distance[i] == INF: # 만약 연결된 간선이 없을시 무한대로 출력
        print('INF')
    else:
        print(distance[i])

