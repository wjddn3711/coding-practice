n = int(input()) # 도시의 개수
dist = list(map(int, input().split())) # 주유소간 거리
price = list(map(int, input().split())) # 주유소의 가격
cost = 0 # 비용을 0으로 초기화
totalDist = sum(dist) # 도시간 총거리
for i in range(n):
    if price[i] == min(price): # 현재 주유소가 최저값 주유소라면
        cost += totalDist*price[i] # 가격은 남은거리*현재주유소가격
        break # 더이상 반복이 필요 없으므로 종료
    else: # 만약 최저값이 아니라면
        driven = 0 # 현재 주유소에서 다음 주유소까지의 주행거리
        for j in range(i+1,n):
            if price[i] > price[j]: # 만약 현재 주유소가 다음 주유소보다 비싸다면
                driven = sum(dist[i:j]) # i번째 주유소에서 j번째 주유소까지의 거리
                totalDist -= driven # 총거리에서 주행거리를 빼준다
                cost += driven*price[i] # j번째 주유소까지의 비용
                break
    if totalDist == 0: break # 총거리를 모두 주행했다면 반복 종료
print(cost)

# 리뷰: 만약 현재 주유소가 최저값 주유소가 아니라면 다음 주유소에 무조건 현재 주유소보다 싼 주유소가 있을
# 것 이므로 만약 최저값 주유소가 아니라면 현재보다 싼 주유소가 나올때까지 반복하며 거리에 따른 비용을 더해준다
# 그리고 주행거리가 총거리와 동일해 졌을때 반복을 종료하여 비용을 받아왔다

