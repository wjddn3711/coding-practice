n,m,k = map(int,input().split())
ar = list(map(int,input().split()))
# 리스트를 내림차순으로 바꾼다. 가장 앞에 오는 수가 max
ar.sort(reverse=True)

# m 번 더하는 것이기 때문에 반복은 m번 해준다
# 더한 값을 받아줄 total 을 0으로 초기화 시켜준다
total = 0
cnt = 0 # max 카운트를 0으로 초기화


m1 = ar[0] # 가장 큰 max
m2 = ar[1] # 두번째로 큰 max

cnt = (m//(k+1))*k
cnt += m%(k+1)

total = m1*cnt
total+= m2*(m-cnt)
print(total)





