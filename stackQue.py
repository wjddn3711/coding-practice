# def solution(progress, speeds):
#     days = list()
#     answer  = list()
#     funcCnt = 1 # 기능 개수
#     for i in range(len(progress)):
#         days.append((100-progress[i])//speeds[i])
#         if (100-progress[i])%speeds!=0: # 수행일자가 소수라면 days +1
#             days[i]+=1
#     comp = days[0] # 첫번째 프로세스가 수행되는 날수를 변수에 담아준다
#     for i in range(1,len(days)):
#         if comp>=days[i]:
#             funcCnt += 1 #기능 개수를 추가 시킨다
#         else:
#             answer.append(funcCnt)
#             comp = days[i] # 비교대상을 days[i]로 바꾸기
#             funcCnt = 1 # 기능 개수를 다시 1로 초기화
#         if i == len(days)-1: # 마지막이라면 answer에 기능 개수를 추가한다
#             answer.append(funcCnt)
#     return answer
#
# progress = list(map(int,input().split()))
# speeds = list(map(int,input().split()))
# print(solution(progress, speeds))

from collections import deque as dq
def solution(progress, speeds):
    days = []
    answer = []
    for i in range(len(progress)):
        days.append((100-progress[i])//speeds[i])
        if (100-progress[i])%speeds[i]!=0: # 수행일자가 소수라면 days +1
            days[i]+=1
    x = dq([days.pop(0)])
    cnt = 1
    while days:
        now = x.pop()
        if now>=days[0]: #현재 수행중인 프로세스가 다음 수행 프로세스보다 클때
            x.append(now) #수행중인 프로세스에 추가해준다
            days.pop(0) #days 에서 빼준다
            cnt+=1 # 기능개수 +1
        else: #현재 수행중인 프로세스가 다음 수행 프로세스보다 작을 때
            x.append(days[0]) # 다음 수행 프로세스가 현재 프로세스
            answer.append(cnt) # 기능개수를 저장해준다
            days.pop(0) #days 에서 빼준다
            cnt = 1 #기능 개수 1로 초기화
        if not days: # days 에 데이터가 없다면
            answer.append(cnt) # 기능 개수를 저장
    return answer

progress = list(map(int,input().split()))
speeds = list(map(int,input().split()))
print(solution(progress, speeds))
#
