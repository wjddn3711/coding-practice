bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]



def solution(bridge_length, weight, truck_weights):
    answer = 0
    stack = [0 for _ in range(bridge_length)]  # 다리 길이만큼 0으로 초기화
    while stack:
        stack.pop(0)
        answer += 1
        if truck_weights:  # 지나갈 트럭이 있다면
            if sum(stack) + truck_weights[0] <= weight:  # 중량을 초과 하지 않는다면
                stack.append(truck_weights.pop(0))  # 트럭에서 꺼내어 스택에 삽입한다
            else:  # 중량을 초과한다면
                stack.append(0)  # 0을 다시 넣어준다
    return answer

print(solution(bridge_length,weight,truck_weights))