def times(n,x):
    if n%x==0: return n//x
    return n//x+1
def solution(answers):
    answer = []
    n = len(answers)
    # 각 학생별 찍는 패턴을 기준으로 시험지의 길이에 맞게 1번부터 3번학생까지의 답안지를 생성한다
    partOne = [1,2,3,4,5]*times(n,5)
    partTwo = [2,1,2,3,2,4,2,5]*times(n,8)
    partThree = [3,3,1,1,2,2,4,4,5,5]*times(n,10)
    score = [0]*3 # 각 학생별 맞췄을때의 점수를 갱신한다
    for i in range(len(answers)): # 각 경우 마다 맞췄을시 스코어를 증가시킨다
        if partOne[i] == answers[i]: score[0]+=1
        if partTwo[i] == answers[i]: score[1]+=1
        if partThree[i] == answers[i]: score[2]+=1
    maxScore = max(score) #세명의 학생중 최대로 많이 맞춘 사람
    for i in range(len(score)): # 최대로 맞춘 사람이 많을경우 최대로 맞힌 사람을 답에 저장
        if score[i]==maxScore: answer.append(i+1)
    return answer

answers = [1,3,2,4,2]
print(solution(answers))

'''
1번 수포자 찍는 방식 :1, 2, 3, 4, 5                 5개
2번              :2, 1, 2, 3, 2, 4, 2, 5         8개
3번              :3, 3, 1, 1, 2, 2, 4, 4, 5, 5   10개
'''