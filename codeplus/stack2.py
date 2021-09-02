n =int(input()) # 스택의 개수
command = list(int(input()) for i in range(n)) # 명령을 저장할 리스트
count = 0
stack = []
ans = []
flag = True # 스택이 올바른지 확인할 징표
for target in command:
    while count<target:         # 만약 타겟이 카운트 보다 작다면
        count +=1 # 타겟까지 카운트를 스텍에 삽입
        stack.append(count) # 스텍에 카운트 삽입
        ans.append('+')

    if stack[-1]==target: # 만약 스택의 탑과 타겟이 같다면
        ans.append('-')
        stack.pop(-1) # 탑을 꺼내준다
    else: # 만약 스택의 탑과 타겟이 같지 않다면
        flag=False #잘못된 스택이다
        break

if flag:
    [print(answer) for answer in ans]
else:
    print('NO')










