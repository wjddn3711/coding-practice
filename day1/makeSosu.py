from itertools import combinations
def isPrime(n):
    for i in range(2,int(n**0.5)+1): #2~루트n까지 한번이라도 나누어 떨어지면 그 수는 소수가 아니다
        if n%i==0:return False
    return True

def solution(nums):
    answer = 0
    combi = list(combinations(nums,3))
    for item in combi:
        if isPrime(sum(item)): answer+=1
        print(sum(item), isPrime(sum(item)))

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    return answer

nums = [1,2,3,4]
print(solution(nums))