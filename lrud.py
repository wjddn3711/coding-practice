n = int(input())

mv = list(map(str,input().split()))
# L,R,U,D 이동시 좌표의 움직임을 x,y를 이용해 표현해보자
fx = ['L','R','U','D']
dx = [0,0,-1,1]
dy = [-1,1,0,0]

# 문제 요구에 따라 여행가는 0,0 에서 출발한다. 다만 문제에서는 0,0이 1,1에 해당된다
x = 1
y = 1
# 총 n 번의 이동 과정을 거치기에 미리 반복을 n번 돌린다 가정한다

for item in mv:
    # 이동 후 좌표 구하기
    for i in range(len(fx)):
        if item==fx[i]:
            nx = x+dx[i]
            ny = y+dy[i]
    # 공간을 벗어나는 경우 무시
    if nx <1 or ny <1 or nx>n or ny>n:
        continue
    # 이동 수행
    x,y = nx,ny
print(x,y)


# for i in range(len(mv)):
#     # 이동할 문자열 받기
#     for j in range(4):
#         # fx의 j 번째 인덱스가 mv와 같다면
#         if mv[i]==fx[j]:
#         # 가장 먼저 지도 바깥으로 벗어 났을 때 무시되는 경우를 생각해보자
#             if x+dx[j] < 1 or y+dy[j]<1 or x+dx[j]>(n+1) or y+dy[j]>(n+1):
#                 continue
#             else:
#                 x = x + dx[j]
#                 y = y + dy[j]
#
# print(x,y)
