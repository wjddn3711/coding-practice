n = int(input())
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,(a%b))

for i in range(n):
    a, b = map(int, input().split())
    if a<b: # 만약 b가 더 크다면
        a,b = b,a # 큰수가 앞에 오도록
    print(int((a*b)/gcd(a,b)))
