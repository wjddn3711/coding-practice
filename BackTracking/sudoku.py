sMap = []
zeroList = []
for i in range(9):
    x = list(map(int,input().split()))
    sMap.append(x)
    for j in range(9):
        if x[j]==0: # 0들의 좌표를 따로 저장해준다
            zeroList.append((i,j))

def isCorrect(x,y):
    possNum = [1,2,3,4,5,6,7,8,9] # 빈칸에 들어올수 있는 경우의 수
    # sMap의 숫자들을 유망한 possNum에서 빼주어 유망한 수들을 초기화한다
    for i in range(9):
        if sMap[x][i] in possNum: # 해당열에 존재하는 수들을 유망한 수의 집합에서 빼준다
            possNum.remove(sMap[x][i])
        if sMap[i][y] in possNum: # 해당행에 존재하는 수들을 유망한 수의 집합에서 빼준다
            possNum.remove(sMap[i][y])
    # 만약 x or y 가 0~2 라면 3으로 나눴을때 몫이 0이다 즉 3까지 반복하여 돌리면 된다는 뜻
    # 만갹 x,y 가 3~5 라면 3으로 나눴을때 몫이 1이며 최종치 6까지 반복하면 된다
    col = (x//3) *3
    row = (y//3) *3
    for i in range(col, col+3): # 열의 범위는 (x//3)*3 ~ ((x//3)+1)*3 이다
        for j in range(row, row+3): # 열의 범위는 (x//3)*3 ~ ((x//3)+1)*3 이다
            if sMap[i][j] in possNum: # 만약 해당 3*3 구역에 포함된 수가 유망한 수들 중에 있다면 제거한다
                possNum.remove(sMap[i][j])
    # print(possNum)
    return possNum # 유망한 수의 조사가 끝났다면 반환해준다

flag = False
def solve(n):
    global flag
    if flag:
        return
    if n == len(zeroList): # n 이 최대 깊이, 즉 마지막 0의 좌표까지 도달했다면 반환한다
        for row in sMap:
            print(*row)
        flag = True
        return

    ar = zeroList[n] # 0 번째 부터 시작하여 제로리스트를 불러온다
    x, y = ar[0],ar[1] # x,y 는 0의 행열 좌표이다
    numbers = isCorrect(x,y) # x,y에 대하여 유망한 수들을 불러온다
    for number in numbers:
        sMap[x][y] = number # 스도쿠 맵에 유망한 수를 삽입한다
        solve(n+1)
        sMap[x][y] = 0 # 만약 유망하지 않다면 백트래킹, 0으로 초기화 한다

solve(0)



