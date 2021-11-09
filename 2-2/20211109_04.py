n = int(input()) # 점의 개수
vector = [list(map(int, input().split())) for _ in range(n)] # n 개의 점의 좌표를 받아온다
vector.sort(key= lambda x:(x[0],x[1])) # x좌표를 기준으로 정렬 같다면 y를 기준으로 오름차순
for x, y in vector:
    print(x,y) # 출력 형식에 맞게 출력해준다
# 리뷰: 파이썬에서 sort 의 key옵션을 통하여 0번째 정렬조건인 x좌표와 다음 정렬 조건 y를 설정하여
# 손쉽게 정렬할 수 있었습니다.