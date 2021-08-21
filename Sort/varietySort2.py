# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.
from collections import Counter as ct
n = int(input())
x = 0
ar = [int(input()) for _ in range(n)]
ar.sort() # 리스트를 오름 차순으로 정렬
last = ct(ar) # 딕셔너리 형태로, { 리스트의 데이터 : 데이터의 개수 } 로 자동 변환
maxCnt = 0 # 카운트최대값의 개수
mc = 0 # 최빈값
for key, value in last.items():
    if value == max(last.values()) and maxCnt==0:
        mc = key
        maxCnt+=1
    elif value == max(last.values()) and maxCnt==1:
        mc = key
        break # 이경우 구하는 즉시 탈출
print(last.most_common(2)[0][0])
print('{:.0f}'.format(sum(ar)/n))
print(ar[n//2])
print(mc)
print(ar[-1]-ar[0])