N=5
stages=[2,1,2,6,2,4,3,3]


def solution(N, stages):
    l = len(stages) # 현재 사람을 뜻한다
    fail = dict() # 딕셔너리로 스테이지별 실패율을 만든다
    for i in range(1,N+1):
        if l!=0:
            f = stages.count(i) # i번째 스테이지에서 탈락한 사람의 수
            fail[i]=f/l # 각 단계는 키값, 벨류는 실패율
            l -= f # 진행하는 수는 기존 인원 - 탈락한 인원
        else:
            fail[i]=0
    # answer = sorted(fail.keys(), reverse=True, key=lambda x:fail[x])
    # value 값인 실패율을 기준으로 내림차순으로 정렬한다
    return sorted(fail, reverse=True, key=lambda x:fail[x])

print(solution(N,stages))
