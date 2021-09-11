import sys
input = sys.stdin.readline

def isprime(n):
    a = [False, False] + [True] * (n - 1)
    primes = []
    for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False
    return primes

def goldBah(n):
    pl = isprime(n) # pl 은 1~n 까지의 소수
    flag = False
    while pl:
        x = pl.pop(0) # 가장 앞에 있는 소수를 꺼낸다
        if len(pl)==0:
            print("Goldbach's conjecture is wrong.")
            break
        if 2*x==n:
            print('{} = {} + {}'.format(n, x, x))
            break
        for i in range(len(pl)//2-1,len(pl)): # 가장 큰 소수부터 더해준다
            if pl[i] + x == n: # 더한 값이 타겟과 동일하면 출력후 탈출
                print('{} = {} + {}'.format(n,x,pl[i]))
                flag = True
                break
        if flag:
            break


while True:
    x = int(input())
    if x==0:
        break
    if x<=4:
        continue
    else:
        goldBah(x)



