import sys
input = sys.stdin.readline
n = int(input()) # n개의 수
A = list(map(int, input().split())) # 비교할 수열
stack = [0]
nge = [-1]*n # 오큰수 저장
for i in range(1,n):
    # for j in range(i+1,n):
    #     if A[i]<A[j]: # 뒤에 있는 수가 크다면 출력 후 탈출
    #         print(A[j],end=' ')
    #         break
    #     if j==n-1: #위의 경우도 아니고 마지막 까지 도달했다면
    #         print(-1, end=' ')
    # if i==n-1: # 마지막 수의 오큰수는 항상 -1 이다
    #     print(-1)
    while stack and A[stack[-1]] < A[i]:
        nge[stack[-1]]=A[i]
        stack.pop()
    stack.append(i)

print(*nge)
