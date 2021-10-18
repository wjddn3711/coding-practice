
lost = [2,4]
reserve = [3]

def solution(n, lost, reserve):
    # for cloth in reserve: # 여벌 체육복을 가져온 학생이 도난당했을 경우를 먼저 고려하여 리스트에서 제거해준다
    #     if cloth in lost:
    #         lost.remove(cloth)
    #         reserve.remove(cloth)
    # set 을 이용한 차집합으로 중복요소를 없애기! (여유체육복을 소지한 학생이 읽어버린 경우를 빼준다)
    r = set(reserve)-set(lost)
    l = set(lost)-set(reserve)

    for cloth in r: # 바로 뒤의 학생이나 앞의 학생이 존재할시 읽어버린 학생 리스트에서 제거
        if cloth-1 in l: l.remove(cloth-1)
        elif cloth+1 in l: l.remove(cloth+1)
        if len(l)==0: break # 읽어버린 친구가 더이상 없다면 반복 탈출
    answer = n-len(l)
    return answer

print(solution(5,lost,reserve))