from itertools import combinations as cb
import sys
input = sys.stdin.readline
n = int(input()) #스타트 팀과 링크 팀의 능력치의 최소값
# 각 선수들의 능력치를 기록
S = [list(map(int,input().split())) for _ in range(n)]
# 각 선수들의 매칭 경우의 수를 받기 위해 선수리스트를 따로 만든다
mem = [i for i in range(n)]
members = list(cb(mem,n//2))
minVal = sys.maxsize  # 초기 최소값 설정

for member in members:
    start = list(member) # 처음 멤버를 스타트 멤버로 초기화한다
    link = list(x for x in mem if x not in member) # link 는 start를 제외한 나머지이다
    startCombi = list(cb(start,2)) # start의 요소가 2명 이상일 때 이를 다시 둘로 나눠 따로따로 계산해야한다
    linkCombi = list(cb(link,2)) # link 팀 또한 동일
    # 두명씩 묶었을 때 능력치를 모두 더해준다
    sTeam,lTeam = 0,0
    for x,y in startCombi:
        sTeam += S[x][y]+S[y][x]
    for x,y in linkCombi:
        lTeam += S[x][y]+S[y][x]
    # s - l 팀이 음수가 될수있기에 절대값으로 계산
    minVal = min(minVal, abs(sTeam-lTeam))

print(minVal)

