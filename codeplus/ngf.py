import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
cnt = Counter(a)
# print(cnt)
# print(cnt.values())
# print(cnt)
stack = [0]
ngf = [-1]*n
for i in range(1,n):
    # if cnt[a[i]]==max(cnt.values()):
    #     print(-1,end=' ')
    # elif i==n:
    #     print(-1,end=' ')
    # else:
    #     for j in range(i+1,n):
    #         if cnt[a[j]]>cnt[a[i]]: #카운트가 더 크다면
    #             print(a[j],end=' ')
    #             break
    #         if j==n-1: # 끝까지 카운트가 더 큰 경우가 없다면
    #             print(-1,end=' ')
    while stack and cnt[a[stack[-1]]]<cnt[a[i]]:
        ngf[stack[-1]]=a[i]
        stack.pop()
    stack.append(i)
print(*ngf)

