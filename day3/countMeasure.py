def measure(num):
    cnt = 0
    for i in range(1,num+1):#1~num까지 나누어 떨어지는 개수를 센다
        if num%i==0: cnt+=1
    if cnt%2==0: #약수의 개수가 짝수라면
        return num #그대로 반환
    return num*-1 #약수의 개수가 홀수라면 -num 을 반환

def solution(left, right):
    answer = 0
    for num in range(left,right+1):
        answer += measure(num)
    return answer

print(solution(24,27))