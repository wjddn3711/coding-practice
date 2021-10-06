A = [1,2]
B = [3,4]

def solution(A,B):
    answer =0 # 초기 누적합계 0으로 초기화
    # 두 배열에서 숫자의 곱이 최소가 되는 경우는 한 배열을 기준으로 최소값과 다른 배열의 최대값을 곱하는 경우이다
    while A: # A를 기준으로 최소값을 골라 그 값을 B의 최대값과 곱하는 경우를 생각해보자
        minVal = min(A) # A의 최소값
        maxVal = max(B) # B의 최대값
        answer += minVal*maxVal #A의 최소값*B의 최대값 (순서는 무관하다)
        A.remove(minVal) # 마지막에 A와 B를 제거함으로 다시 while(조건)에서 만약 A배열이 비었다면 아래 return수행
        B.remove(maxVal)
    return answer

def solution2(A,B):
    answer =0
    A.sort(reverse=True) # A는 내림차순 (최대값 -> 최소값 순)
    B.sort() # B는 오름차순 (최소값 -> 최대값 순)
    for i in range(len(A)): #A와 B의 길이 동일
        answer+= A[i]*B[i] # 위에서 정렬을 하였기 때문에 그대로 곱하면 최대값*최소값 형태가 된다
    return answer

print(solution2(A,B))
print(solution(A,B))


