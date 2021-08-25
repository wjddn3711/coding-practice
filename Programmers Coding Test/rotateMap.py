
rows, columns = 3,3
queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
def solution(rows, columns, queries):
    # 1 ~ row*column 까지 map 생성
    ar = [[row * columns + col + 1 for col in range(columns)] for row in range(rows)]
    answer = []

    for t, l, b, r in queries:
        top, left, bottom, right = t - 1, l - 1, b - 1, r - 1 # 인덱스 값으로 표현하기 위해 -1 해준다
        minVal = ar[top][left] # 좌측 상단을 따로 빼준다
        minimum = minVal # 좌측 상단값을 임시로 최소값이라 지정한다

        for y in range(top, bottom): # 좌측 상단에서 하단까지 값을 바꿔준다
            value = ar[y + 1][left]
            ar[y][left] = value
            minimum = min(minimum, value) # 최소값을 구한다

        for x in range(left, right): # 좌측 하단부터 우측 하단까지 값을 바꿔준다
            value = ar[bottom][x + 1]
            ar[bottom][x] = value
            minimum = min(minimum, value)

        for y in range(bottom, top, -1): # 우측 하단부터 우측 상단까지 값을 바꿔준다
            value = ar[y - 1][right]
            ar[y][right] = value
            minimum = min(minimum, value)

        for x in range(right, left, -1): # 우측 상단부터 좌측 상단까지 값을 바꿔준다
            value = ar[top][x - 1]
            ar[top][x] = value
            minimum = min(minimum, value)
        print(ar)
        ar[top][left + 1] = minVal # 좌측+1 상단 값은 초기에 저장했던 값
        answer.append(minimum) # 최종 최소값을 저장한다

    return answer






print(solution(rows, columns, queries))