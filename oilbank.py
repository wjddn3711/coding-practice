
n = int(input())
lgth = list(map(int,input().split()))
cost = list(map(int,input().split()))

oil=0
# 총 필요한 키로수
for item in lgth:
    oil+=item

# 처음 비교할 대상을 정한다 순차적으로 가장 앞에있는 주유소에서 가득채워 각 도시들을 다 들린다 했을 때
# d1 = 첫주유소 비용 * 총 거리수가 된다
d1 = cost[0]*oil

# 필요한 최소 거리 수를 초기화한다
des = 0
# leng은 i 번째 까지 온 거리이며 0으로 우선 초기화한다
leng = 0
# i 는 첫번째를 제외하고 주유소의 개수 만큼 반복
for i in range(1,len(cost)):
    # len = [ 2, 3, 1 ] 일 때 i 번째 인덱스는 1 부터 시작하기에 1을 빼준다
    leng += lgth[i-1]
    # 만약 (해당 주요소 비용*남은 거리수) 가 ((해당 주요소 비용*다음주유소까지 거리)+(다음 주요소비용*남은거리수)) 보다 크다면
    # des에는 (해당 주유소* 다음주유소까지의 거리를 더해준다)
    if d1> cost[i-1]*lgth[i-1]+cost[i]*(oil-leng):
        des+=cost[i-1]*lgth[i-1]
        # d1에서 다음 해당 주요소는 다음 주유소* 남은 거리수이기에
        d1 = cost[i]*(oil-leng)
    else:
        # 만약 (해당 주요소 비용*남은 거리수) 가 ((해당 주요소 비용*다음주유소까지 거리)+(다음 주요소비용*남은거리수)) 보다 작다면
        # des 에는 해당 주유소*남은 거리수 를 더해준다, 이경우 더이상 반복할 필요가 없기에 break를 통해 반복을 중지한다
        des+=d1
        break

print(des)