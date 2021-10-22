# import sys
# from itertools import combinations
nums= [3,1,3,2]
def solution(nums):
    # x= list(combinations(nums,len(nums)//2))
    # answer = sys.maxsize*-1 # 최소 값으로 설정하고 맥스 값을 찾는다
    # for item in x:
    #     answer = max(answer,len(set(item)))
    #     # set을 통해 중복을 제거한 길이를 통해 최대 종류값을 갱신한다
    answer = min(len(set(nums)), len(nums)//2)
    # nums 를 통해 최대로 만들수 있는 종류수는 중복을 제거한 포켓몬의 수와 같다. 하지만
    # 포켓몬은 최대 n//2 만큼 뽑을 수 있기 때문에 이 경우와 비교를 해야한다
    # 만약 수가 고르게 있는 nums 같은 경우 len(set(nums))가 더 클 것이고
    # 반대의 경우 len(nums) 가 더 클 것이다. 만약 2,2,2,3,3,3,3,2 일 경우
    # len(nums)//2 는 4 이며 len(set(nums)) 는 2가 된다. 이 경우는 최대 종류값은
    # len(set(nums))가 된다 . 그렇다면 1,2,3,4,5,6 일 경우?  전자는 3, 후자는 6
    # 즉 전자가 되야 하기 때문에 이 두값중 최소값을 출력하면 된다
    return answer
