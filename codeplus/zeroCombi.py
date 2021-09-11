from itertools import combinations
def factorial(n):
    if n in [0,1]:
        return 1
    else:
        return n*factorial(n-1)
n,m = map(int,input().split())
nCm = str(int(factorial(n)/((factorial(n-m)*factorial(m))))) # 조합의 수를 구한다
# 조합은 n!/((n-m)!*m!)) 이다. 이를 int로 바꿔 소수점이하를 제거하고, str로 바꾸어 끝자리검사를 실시한다


cnt = 0
for i in reversed(range(len(nCm))):
    if nCm[i]=='0':
        cnt+=1
    else:
        break
print(cnt)