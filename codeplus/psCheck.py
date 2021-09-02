n = int(input()) # 명령 개수
ps = [input() for _ in range(n)]

def isCorrect(string):
    lct = string.count('(')
    rct = string.count(')')
    if lct != rct: #왼쪽 괄호, 오른쪽 괄호 개수가 맞지않다면
        return print('NO')
    elif string[0]==')': # 만약 오른쪽 괄호로 시작한다면
        return print('NO')
    else:
        stack = []
        for i in range(0,len(string)):
            if len(stack)==0: #만약 스택이 비어있다면
                stack.append(string[i]) # 스택이 삽입한다
            elif stack[-1]=='(' and string[i]==')': # 만약 새로운 괄호가 스택에 삽입된 마지막 괄호와 짝이 맞다면 스택에서 빼준다
                stack.pop(-1)
            else:
                stack.append(string[i])
        if len(stack)>0: #스택에 괄호가 하나라도 존재한다면
            print('NO')
        else:
            print('YES')

for string in ps:
    isCorrect(string)
