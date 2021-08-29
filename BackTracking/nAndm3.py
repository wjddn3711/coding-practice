from itertools import product
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
ar = [i for i in range(1,n+1)] # 1~ n 까지의 수열 생성
x = list(product(ar,repeat=m)) # x는 ar 에서 중복을 허용하며 m 개를 뽑는 경우의 수
# 출력 부분
for i in range(len(x)):
    for j in range(len(x[i])):
        print(x[i][j], end=' ')
    print()