from string import ascii_lowercase
priorities = [2, 1, 3, 2]
location = 2
stack = []

def solution(priorities, location):
    answer = 0
    m = max(priorities) # 우선순위가 가장 높은것 초기화
    while priorities:
        var = priorities.pop(0) # 가장 앞에 있는 수를 꺼낸다
        if var==m: # 가장 앞에 있는 수가 최대값이라면
            answer+=1 # 정렬후 출력 되는 수 +1
            if location==0: break # 구하고자 하는 수의 위치가 0 이고 max라면 탈출
            else: location-=1 # 한칸 앞으로 땡긴다
            m = max(priorities) # max 값 초기화
    # 구하고자 하는 수의 위치가 0이 아니라면 위치 -1 (하나를 꺼내어 뒤로 옮겨졌기 때문에 타겟이 바뀌게 된다
        else: # 가장 앞에 있는 수가 최대값이 아니라면
            priorities.append(var) # 뒤로 옮긴다
            if location==0: # 최대값이 아닌데 위치가 0이라면 맨뒤로 옮겨준다 즉, len-1
                location=len(priorities)-1
            else: #최대값이 아니고 구하고자 하는 위치가 0이 아니라면
                location-=1 # 한칸 앞으로 땡긴다
    return answer

print(solution(priorities,location))