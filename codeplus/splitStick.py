# 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다.
# - 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓는다.
# 각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.
# 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다.

# 시작 괄호 를 만날때 마다 막대기의 길이를 가늠한다다
import sys
input = sys.stdin.readline
stack = []
count = 0
stick = input() # 쇠 막대기
for i in range(len(stick)):
    if stick[i] == '(': # 시작 괄호라면 스택에 삽입하여 길이를 늘려준
        stack.append('(')
    else: # 닫는 괄호라면
        if stick[i-1]=='(': # 이전 괄호가 여는 괄호라면 한쌍이 만나 레이저가 된다
            stack.pop() # 한 쌍을 이루었기에 ( 를 꺼내준다
            count += len(stack)
        else: # 이전 괄호가 닫는 괄호라면
            stack.pop() # 막대가 있다는 뜻이므로 길이 +1 을 해준다
            count += 1
print(count)