prices = [1,2,3,2,3]

def solution(prices):
    answer = [0]*len(prices) # 각 시점당 0으로 초기화해준다
    for i in range(len(prices)-1): # 마지막 인덱스 값은 항상 0이기에 반복에 넣지 않는다
        if prices[i]>prices[i+1]:# 만약 앞의 값이 바로 뒤에 값보다 크다면
            answer[i]+=1 # 1초동안은 가격이 떨어지지 않은 것으로 보고 +1 해주고 다음 반복으로
            continue
        for j in range(i+1,len(prices)):
            if prices[i] <= prices[j]:
                answer[i]+=1 # 만약 가격이 떨어지지 않으면 +1
            else: break # 만약 가격이 떨어졌다면 반복 탈출
    return answer

print(solution(prices))