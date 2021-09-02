import sys
input = sys.stdin.readline
n = int(input()) # 명령의 개수
queue =[] #FIFO
result = []
command = list(input().split() for _ in range(n))
for i in range(n):
    # command = input().strip()
    if command[i][0] =='push': #정수 X를 큐에 넣는 연산
        queue.append(command[i][1])
    elif command[i][0] =='pop': #큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if queue:
            print(queue.pop(0)) #큐가 비어있지 않다면 가장 먼저 들어온 수를 꺼낸다
        else:
            print(-1)
    elif command[i][0]=='size': #큐에 들어있는 정수의 개수를 출력한다.
        print(len(queue))
    elif command[i][0]=='empty': #큐가 비어있으면 1, 아니면 0을 출력한다
        if queue: #큐가 비지 않았다면
            print(0)
        else:
            print(1)
    elif command[i][0]=='front': #큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command[i][0]=='back': #큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if queue:
            print(queue[-1])
        else:
            print(-1)