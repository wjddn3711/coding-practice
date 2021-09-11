from string import ascii_uppercase
import sys
input = sys.stdin.readline
n = int(input()) # 피 연산자의 개수
string = input()
alphaList = list(ascii_uppercase)[:n] # n 번째 까지의 알파벳 리스트
num = list(input() for _ in range(n)) # 알파벳에 해당하는 숫자
stack =[]
post =[]
# 입력받은것을 리스트 형태로 변환하고 알파뱃을 숫자로 변환하여 post 에 저장한다
for i in range(len(string)):
    if string[i] in alphaList: # 알파뱃이라면
        post.append(num[alphaList.index(string[i])])
    else:
        post.append(string[i])
print(post)

for i in range(len(post)):
    if post[i] in num: #만약 숫자라면
        stack.append(post[i])
    elif post[i] == '+':
        a = float(stack.pop())
        b = float(stack.pop())
        stack.append(str(a+b))
    elif post[i] == '-':
        a = float(stack.pop())
        b = float(stack.pop())
        stack.append(str(b - a))
    elif post[i] == '/':
        a = float(stack.pop())
        b = float(stack.pop())
        stack.append(str(b / a))
    elif post[i] == '*':
        a = float(stack.pop())
        b = float(stack.pop())
        stack.append(str(a * b))
print('{:.2f}'.format(float(stack[0])))