import sys
input = sys.stdin.readline
n = int(input()) # 명령어의 개수
commands = [list(map(str,input().split())) for _ in range(n)]
stack = []
for command in commands:
    if command[0] =='push':
        stack.append(int(command[1]))
    elif command[0] =='top': # stack 의 가장 위쪽을 출력한다
        if len(stack)==0: #스택이 비어있으면 -1을 출력
            print(-1)
        else:
            print(stack[-1])
    elif command[0] =='size':
        print(len(stack)) # stack의 길이를 출력
    elif command[0]=='empty':
        if len(stack)>0: #stack 이 비어있지 않다면 0을 출력
            print(0)
        else:
            print(1)
    elif command[0] == 'pop':
        if len(stack)==0: # 만약 stack 이 비어있다면 -1을 출력
            print(-1)
        else: # 비어있지 않다면 스택에서 하나를 꺼내고 그 수를 출력
            x = stack.pop(-1)
            print(x)


