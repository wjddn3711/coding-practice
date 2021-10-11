from itertools import combinations
'''
에라토스테네스의 체에 의한 소수 구하기
1. 2부터 n 까지의 소수를 구한다 하였을 때, n의 최대약수는 sqrt(n)이다
2. 2부터 시작하여 수의 배수를 모두 걸러준다.
3. 즉, 2 부터 sqrt(n)까지 반복하여 약수들의 배수를 모두 걸러준다
4. 최종적으로 걸러지지 않은 수들은 모두 소수이다
'''
nums = [1,2,7,6,4]

def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    isPrime = [True] * n
    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)+1
    for i in range(2, m):
        if isPrime[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i를 제외하고 i의 배수들은 모두 걸러준다
                isPrime[j] = False
    # 소수 목록 산출
    return [i for i in range(2, n) if isPrime[i] == True]

def solution(nums):
    primeList = prime_list(3000)
    # nums 의 각 원소는 1 이상 1000 이하의 자연수이며 3개를 뽑기 때문에 최대 nums의 합은 3000이다.
    # 즉 2에서 3000까지의 소수들을 모두 구한뒤 시작한다
    primeCnt =0
    # combinations 를 이용하여 n개의 수중에서 r개를 뽑는 nCr을 만든다
    cases = list(combinations(nums,3)) #[(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
    # 각 케이스 별로 그들의 합이 소수인지 판별하여 소수인 경우의 수를 카운트 하여 리턴하자
    for case in cases:
        if sum(case) in primeList: # 만약 케이스의 합이 소수리스트에 있다면 카운트 +1
            primeCnt+=1
    return primeCnt

print(solution(nums))
'''
리뷰: 이전에 소수를 구하는 문제를 어느정도 접해봐서 생각했던 대로 구현할 수 있었습니다. 그리고 경우의 수를 구하는 것을 쉽게 해주는 combinations 라이브러리는
모든 경우의 수를 탐색하여 판별하는 문제에서 자주 등장하기 때문에 이번 기회에 다시 사용하면서 좀 익숙해진것 같습니다. 에라토스테네스의 체 같은 경우 일반적으로 
떠올릴 수 있는 소수 판별법인 2부터 타겟 숫자까지를 나눴을 때 한번 밖에 안나눠떨어지면 소수이다 하는 방법은 O(n^2)인 반면 에라토스테네스의 체를 이용할 경우
O(Nlog(logN)으로 줄일 수 있기 때문에 확연한 차이를 보여준다. 이는 1000 단위를 넘어서는 순간부터는 O(n^2)의 방법을 사용할 경우 제시간에 문제가 도출되지
않는 점을 어느정도 개선할 수 있다 생각하여 좋았다. n까지의 최대약수가 루트n 이라는 점은 다소 이해하기 어려운 개념이였지만 계속 활용해나가며 익숙해지도록 노력
해야겠다 
'''