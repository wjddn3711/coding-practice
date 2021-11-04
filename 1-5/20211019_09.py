price, money, count = 3,20,4

def solution(price, money, count):
    lPrice,cnt = 0,1 # 최종 가격과 이용횟수 초기화, 이용횟수는 첫시작이 1
    while cnt<=count: # 이용횟수 동안의 총 가격 계산
        lPrice += price*cnt # 최종 가격 = 기존가격* N번째
        cnt+=1
    if money>=lPrice: answer=0 # 금액이 모자라지 않다면 0을 반환
    else: answer=lPrice-money # 금액이 모자라다면 모자란 금액 반환
    return answer

print(solution(price,money,count))
