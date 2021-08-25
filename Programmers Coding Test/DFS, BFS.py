# n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나
# 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.
from collections import deque
numbers = [1, 1, 1, 1, 1]
target = 3

def solution(numbers, target):
    answer = 0
    n = len(numbers)
    q = deque()
    q.append([0,0]) # 시작 합계와 시작 인덱스를 표현
    while q:
        total, indx = q.popleft() # 현재 합계와 현재 index값을 불러온다
        if indx == n: # 만약 현재 인덱스가 마지막 인덱스라면
            if total == target: # 현재 합계가 타겟과 일치한다면
                answer+=1 # 정답 +1
        else: # 아직 마지막 index까지 더하지 않았다면
            q.append((total+numbers[indx],indx+1)) #토탈에 현재 인덱스 값을 추가해주고, 인덱스 +1
            q.append((total-numbers[indx],indx+1)) #토탈에 현재 인덱스 값을 빼주고, 인덱스 -1

    return answer

print(solution(numbers,target))

# from itertools import product
# def solution(numbers, target):
#     l = [(x, -x) for x in numbers]
#     s = list(map(sum, product(*l)))
#     return s.count(target)