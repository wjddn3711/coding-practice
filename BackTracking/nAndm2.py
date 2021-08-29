
from itertools import combinations as combi
import sys
input = sys.stdin.readline
n,m = map(int, input().split()) # 1~n 까지, m 번 고를 때
ar = [i for i in range(1,n+1)] # 1~N 까지의 수열을 생성한다
x=list(combi(ar,m)) # combinations 를 활용하여 리스트에서 m번 고르는 경우의 수를 리스트 형태로 x에 저장한다
for i in range(len(x)): # x 의 길이만큼
    for j in range(len(x[i])): # x 의 데이터를 하나씩 꺼내준다
        print(x[i][j], end=' ')
    print()