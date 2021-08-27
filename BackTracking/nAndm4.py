from itertools import combinations_with_replacement as cr
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
ar = [i for i in range(1,n+1)] # 1~n까지의 수열 생성
x = list(cr(ar,m)) # x 는 중복을 포함하여 ar에서 m 개를 뽑지만 순서가 없으므로 한번 나온 조합은 포함하지 않는다
for i in range(len(x)):
    for j in range(len(x[i])):
        print(x[i][j], end =" ")
    print()