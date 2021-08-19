n = int(input())
ar=[int(input()) for _ in range(n)]

x = 0 #최빈값
ar.sort()
f = [0]*(1+ar[-1]-ar[0]) # 카운트를 저장할 공간
fw = [i for i in range(ar[0],ar[-1]+1,1)] # 카운트의 인덱스가 되는 공간
for i in range(n):
    f[fw.index(ar[i])]+=1
check = 0
if f.count(max(f)) >=2: # count 의 맥스값이 2개 이상일때 두번째 숫자 출력
    for i in range(len(f)):
        if f[i]==max(f) and check ==0: # i번째 인덱스 값이 맥스값이라면 check +1
            check+=1
            continue
        if f[i]==max(f) and check==1: # 두번째 맥스값찾기
            x = fw[i]
            break
else:
    x = ar[0]

print('{:.0f}'.format(sum(ar)/n))
print(ar[n//2])
print(x)
print(ar[-1]-ar[0])
