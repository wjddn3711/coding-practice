# from collections import deque
# string = input() # 기존 문자열을 받아온다
# n = int(input()) # 명령의 개수를 저장한다
# commands = [list(map(str,input().split())) for _ in range(n)] #n 번 동안 명령을 저장한다
# ar = []
#
# ns = string.strip()
# for char in ns:
#     ar.append(char)
# start = len(ar) # 인덱스의 끝 부터 시작한다
# for i in range(n):
#     if commands[i][0] == 'L': # 커서를 왼쪽으로 한칸 옮김
#         start-=1
#         if start<=0:
#             start = 0
#     elif commands[i][0] == 'D': # 커서를 오른쪽으로 한칸 옮김
#         start+=1
#         if start>=len(ar):
#             start = len(ar)
#     elif commands[i][0] == 'B': # 커서 왼쪽에 있는 문자를 삭제함
#
#         if start<=0: # 만약 커서가 맨앞에 있다면
#             continue # 무시
#         else:
#             start-=1
#             ar.pop(start)
#     elif commands[i][0] == 'P': # p뒤의 문자를 커서왼쪽에 삽입
#         if start<=0:
#             start=0
#
#         ar.insert(start,commands[i][1])
#         start+=1 # start 1 증가
# nar = deque(ar)
# while nar:
#     print(nar.popleft(), end='')
# import sys
# input = sys.stdin.readline
# string = input().strip() # 기존 문자열을 받아온다
# n = int(input()) # 명령의 개수를 저장한다
# # commands = [list(map(str,input().split())) for _ in range(n)] #n 번 동안 명령을 저장한다
# start = len(string) # 인덱스의 끝 부터 시작한다
# for i in range(n):
#     command = input().split()
#     if command[0] == 'L': # 커서를 왼쪽으로 한칸 옮김
#         start-=1
#         if start<=0:
#             start = 0
#     elif command[0] == 'D': # 커서를 오른쪽으로 한칸 옮김
#         start+=1
#         if start>=len(string):
#             start = len(string)
#     elif command[0] == 'B': # 커서 왼쪽에 있는 문자를 삭제함
#
#         if start<=0: # 만약 커서가 맨앞에 있다면
#             continue # 무시
#         else:
#             start-=1
#             string = string[:start]+string[start+1:]
#     elif command[0] == 'P': # p뒤의 문자를 커서왼쪽에 삽입
#         if start<=0:
#             start=0
#         # start+=1 # start 1 증가
#         string = string[:start]+command[1]+string[start:]
#         start+=1
# print(string)

import sys
input = sys.stdin.readline
string = list(input().strip()) # 기존 문자열을 받아온다
result = []
n = int(input()) # 명령의 개수를 저장한다
for i in range(n):
    command = input().strip() # 0번째는 커맨드, 2는 삽입할 문자
    if command[0]=='P':
        string.append(command[2])
    elif command[0]=='L' and string!=[]: # string 이 비어있다면 넘길수 없다
        result.append(string.pop()) # 커서가 왼쪽으로 움직였다면 기존 스트링에서 마지막 데이터를 다른 리스트로 넘긴다
    elif command[0]=='D' and result!=[]: # result 가 비어있다면 넘길수 없다
        string.append(result.pop()) # 커서가 오른쪽으로 움직였다면 기존 스트링에 다른 리스트의 마지막 데이터를 넘긴다
    elif command[0]=='B' and string!=[]: # string 이 비어있다면 pop 할 수 없다
        string.pop() # 없애는 거라면 그냥 기존 리스트에서 제거한다
print(''.join(string+list(reversed(result))))