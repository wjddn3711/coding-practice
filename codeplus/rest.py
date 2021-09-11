import sys
input = sys.stdin.readline
A,B,C = map(int,input().split()) # a,b,c 받아오기
print(((A+B)%C))
print(((A%C)+(B%C))%C)
print(((A*B)%C))
print(((A%C)*(B%C))%C)

