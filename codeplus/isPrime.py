n = int(input()) # n번 입력받는다
numbers = list(map(int,input().split()))

def isPrime(numbers):
    prime = 0
    for num in numbers:
        cnt = 0
        for i in range(1,num+1): #1~num까지 나눠준다
            if num%i==0:
                cnt+=1
        if cnt==2: #1이나 자기 자신으로만 나눠진 경우
            prime+=1
    return prime

print(isPrime(numbers))


