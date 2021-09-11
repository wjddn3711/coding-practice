import sys
input = sys.stdin.readline
x, y = map(int, input().split()) # 숫자의 범위
target = [i for i in range(x,y+1)] # x~y까지 숫자를 리스트로 저장

for number in target:
    cnt = 0
    for i in range(2,number): #타겟의 길이만큼 1~자기자신까지
        if number%i==0:
            break
        if i==number-1:
            print(number)
    # if cnt==2: # 자기 자신과 1로만 나눠 떨어지는 경우
    #     print(number)
