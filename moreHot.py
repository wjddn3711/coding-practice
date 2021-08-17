# 스코빌 지수가 1인 음식과 2인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
# 새로운 음식의 스코빌 지수 = 1 + (2 * 2) = 5
# 가진 음식의 스코빌 지수 = [5, 3, 9, 10, 12]
# 스코빌 지수가 3인 음식과 5인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    # pivot = heapq.heappop(scoville) # 스코빌에서 가장 첫번째 값을 피봇으로 설정
    while scoville:  # 스코빌의 데이터가 없을때 까지 반복
        x = heapq.heappop(scoville)
        if x >= K:  # 스코빌의 가장 작은 값이 K를 초과한다면 반복 종료
            break
        if not scoville:
            answer = -1
            break
        y = heapq.heappop(scoville)
        heapq.heappush(scoville,x+2*y)
        answer+=1

    return answer

scoville = [1,2,3,9,10,12]
K=50
print(solution(scoville,K))

