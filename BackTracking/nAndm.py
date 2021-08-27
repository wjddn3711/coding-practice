# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

from itertools import permutations
n,m = map(int, input().split()) # 1~n 까지, m 번 고를 때
ar = [i for i in range(1,n+1)] # 1~N 까지의 수열을 생성한다
x=list(permutations(ar,m)) # permutations 를 활용하여 리스트에서 m번 고르는 경우의 수를 리스트 형태로 x에 저장한다
print(x)
for i in range(len(x)): # x 의 길이만큼
    for j in range(len(x[i])): # x 의 데이터를 하나씩 꺼내준다
        print(x[i][j], end=' ')
    print() # 한열이 끝났다면 띄어쓰기를 한다
