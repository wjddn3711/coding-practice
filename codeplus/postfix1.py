from string import ascii_uppercase
# postfix 는 괄호안의 수식을 괄호 오른쪽으로 빼는 것임
import sys
input = sys.stdin.readline
string = input() # 후위 표기식으로 바꿀 식
pf = ''
stack = []
# print(list(ascii_uppercase))
for i in range(len(string)):
    if string[i].isalpha():
        pf+=string[i]

    else:
        if string[i]=='(': # 시작괄호를 만나면 스택에 삽입한다
            stack.append(string[i])
        elif string[i] in ['*','/']: # 만약 곱하기나 나누기라면
            while stack and stack[-1] in ['*','/']: # 스택이 비어있지 않고 스택의 탑이 먼저 들어온 * 나 / 연산자라면
                pf+=stack.pop() # 스택에 먼저 들어온 * 나 / 연산자를 더해준다
            stack.append(string[i])
        elif string[i] in ['+','-']: # 만약 더하기나 빼기라면
            while stack and stack[-1] != '(': # 우선 순위가 가장 낮기에 앞에 ) 가 오는 경우를 제외하고는 결과에 더해준다
                pf+=stack.pop()
            stack.append(string[i])
        else: # ')' 인 경
            while stack and stack[-1] != '(': # 스택안의 연산자를 하나씩 꺼내 결과에 넣어준다
                pf+=stack.pop()
            stack.pop() # ( 를 꺼내준다
while stack:
    pf+=stack.pop() # 스택에 남아있는 연산자를 더해준다
print(pf)