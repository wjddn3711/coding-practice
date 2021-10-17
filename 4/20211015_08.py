def ma(edges,nodeMap):
    global cnt # 엣지를 돌때 동안 카운트가 바뀌기에 카운트를 전역변수로
    x,y = edges.pop(), edges.pop() # 엣지에서 꺼낸 두 값을 x 와 y에 저장
    if a[x]==0 or a[y]==0: return # 둘중 하나가 가중치가 0이라면 바로 탈출
    # 리프 노드를 우선순위로 놓는다
    prior = x if len(nodeMap[x]) ==1 else y
    other = x if prior!=x else y # 우선순위 노드가 아닌것을 other로 설정
    while True:
        # 우선순위 노드를 0으로 만들어 준다
        if a[prior]<0 : # 만약 가중치가 음수라면 +1을 해준다
            a[prior] += 1  # 우선순위 노드는 +1
            a[other] -= 1  # other 는 -1
        else: # 만약 가중치가 음수가 아니라면
            a[prior] -= 1
            a[other] += 1
        cnt +=1
        if a[prior] == 0: break # 만약 가중치가 0이라면 탈출
    return cnt

a = [-5,0,2,1,2]
edges = [[0,1],[3,4],[2,3],[0,3]]
cnt = 0
def solution(a, edges):
    nodeMap = [[] for _ in range(len(a))] # 각 노드의 연결된 노드를 저장할 맵 생성
    for i in range(len(edges)):
        nodeMap[edges[i][0]].append(edges[i][1]) # 연결된 노드를 저장
        nodeMap[edges[i][1]].append(edges[i][0])
    # 각 노드를 방문하여 연결된 노드들을 저장
    for i in range(len(edges)): # 엣지 방문하여 카운트 시작
        ma(edges[i],nodeMap)
    if cnt==0: answer=-1 # 만약 cnt가 0이라면 답은 -1로
    else: answer = cnt # 아니라면 답은 카운트
    return answer

print(solution(a,edges))