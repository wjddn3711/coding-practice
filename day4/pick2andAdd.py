numbers =[2,1,3,4,1]
from itertools import combinations
def solution(numbers):
    answer = []
    # numbers.sort() # 먼저 숫자들이 담긴 리스트를 오름차순으로 정렬시킨다
    nList = list(combinations(numbers, 2))
    for item in nList:
        if sum(item) not in answer:
            answer.append(sum(item))
    # for i in range(len(numbers)): # 숫자들중 작은 순으로 담아준다
    #     for j in range(i+1,len(numbers)): # 앞서 뽑은 수를 제외하고 다른 수를 뽑는다
    #         if numbers[i]+numbers[j] not in answer: # answer 리스트에 없는 수라면 담아준다
    #             answer.append(numbers[i]+numbers[j])
    return sorted(answer)

print(solution(numbers))