sizes = [[10,7],[12,3],[8,15],[14,7],[5,15]]

def solution(sizes):
    s = len(sizes) # 샘플 명함개수
    for i in range(s):
        if sizes[i][0] > sizes[i][1]: # 둘중 더 큰 값이 우측에 오도록 바꿔준다
            sizes[i][0],sizes[i][1]=sizes[i][1],sizes[i][0]
    sizeS = max(sizes)[0] # 둘중 작은 값들의 집합중 가장 큰값
    sizeB = max(sizes, key=lambda x:x[1])[1] # 둘중 큰 값들의 집합중 가장 큰값
    answer = sizeB*sizeS # 지갑의 크기를 답으로 넘겨준다
    return answer

print(solution(sizes))