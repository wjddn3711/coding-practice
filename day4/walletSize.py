sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]

def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0]>sizes[i][1]: # 만약 앞의 값이 더 크다면 우측에 큰값이 오도록 바꾼다
            sizes[i][0],sizes[i][1] = sizes[i][1],sizes[i][0]
    maxX = max(sizes)[0]
    maxY = max(sizes, key=lambda x: x[1])[1]
    answer = maxX*maxY
    return answer

print(solution(sizes))