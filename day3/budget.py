d = [2,2,3,3]
def solution(d, budget):
    answer = 0
    d.sort() # d 를 오름차순으로 정렬해준다
    payed = 0
    for item in d:
        payed += item # 구매해준 케이스
        if payed > budget: break # 예산을 초과한다면 탈출
        answer+=1 # 이미 구매 완료된 부서의 개수
    return answer

print(solution(d,budget=10))