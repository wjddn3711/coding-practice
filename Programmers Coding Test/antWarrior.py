n = int(input())
house = list(map(int,input().split()))

# def foodCnt(house):
#     maxH = 0
#     for i in range(len(house)):
#         start = house[i]
#         if i+1 == len(house)-1:break
#         for j in range(len(house)):
#             if i==j: continue
#             if j==i-1 or j==i+1: continue# 인접한 곳이라면 무시
#             start += house[j]
#         maxH = max(maxH,start)
#     return maxH
#
# print(foodCnt(house))

# 앞서 계산된 결과룰 저장하기 위한 dp 테이블을 초기화
d = [0]*100
# 다이나믹 프로그래밍 진행 (보텀업)
d[0] = house[0]
d[1] = max(house[0],house[1])
for i in range(2,n):
    d[i] = max(d[i-1],d[i-2]+house[i])
print(d[n-1])
