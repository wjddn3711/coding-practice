# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
from collections import deque as dq
import sys
input = sys.stdin.readline
n = int(input()) # 명령의 개수를 저장할 리스트
deque = dq()
for i in range(n):
    command = list(map(str,input().split())) # 명령을 저장한다
    if command[0]=='push_front': # 정수 X를 덱의 앞에 넣는다
        deque.appendleft(command[1]) # X를 가장 앞에 삽입
    elif command[0]=='push_back': # 정수 X를 덱의 뒤에 넣는다.
        deque.append(command[1])
    elif command[0]=='pop_front': #덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다
        if len(deque) > 0 : # 만약 데크가 비어있지 않다면
            print(deque.popleft())
        else: #만약 데크가 비어있다면
            print(-1)
    elif command[0]=='pop_back':#덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다
        if len(deque) > 0 : # 만약 데크가 비어있지 않다면
            print(deque.pop())
        else: #만약 데크가 비어있다면
            print(-1)
    elif command[0]=='size': #덱에 들어있는 정수의 개수를 출력한다.
        print(len(deque))
    elif command[0]=='empty': #덱이 비어있으면 1을, 아니면 0을 출력한다.
        if len(deque) > 0: # 비어있지않다면
            print(0)
        else:
            print(1)
    elif command[0]=='front': #덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다
        if len(deque) > 0: # 비어있지않다면
            print(deque[0])  # 출력
        else:
            print(-1)
    elif command[0]=='back': #덱의 가장 뒤에 있는 정수를 출력한다
        if len(deque) > 0:  # 비어있지않다면
            print(deque[-1])
        else:
            print(-1)

