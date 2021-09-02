
n = int(input()) # 명령의 개수를 입력받는다
commands = [list(map(str,input().split())) for _ in range(n)] # 공백을 기준으로 각 command를 저장한다
for command in commands:
    for i in range(len(command)): # 명령의 길이만큼 반복한다
        for j in range(len(command[i])-1,-1,-1): #각 문자열의 길이 만큼 반복
            print(command[i][j], end='')
        print(end=' ')
    print()