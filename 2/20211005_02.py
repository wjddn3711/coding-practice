def calculator(x,y,z):
    result = 0 # 결과값을 0 으로 초기화
    # 연산자가 +,-,/,* 일 때를 구분하여 연산을 진행후 반환한다
    if z == '+': result =x+y
    elif z == '-': result =x-y
    elif z == '*': result =x*y
    else: result =x/y
    return result
while True: # 파이썬에는 do-while 이 없기 때문에 while True와 break 를 통해 0 0 0 입력시 탈출 할 수 있도록 해준다
    print('수식 (0 0 0 입력 시 종료)?',end='')
    x,z,y = input().split() # 파이썬의 기본 입력 형태는 문자열이다. 문자열로 x,y,z를 받아온다
    if x=='0' and y=='0' and z=='0': break # 만약 x,y,z 모두 0이라면 종료 되도록 break
    print(calculator(float(x),float(y),z)) # 문자열x,y 를 실수형 float으로 변환후 함수로 넘겨준다

def calculator2(s):
    return eval(s) # eval 함수는 연산자와 수로 이루어진 문자열을 자동 계산하여 반환한다
while True:
    print('수식 (0 0 0 입력 시 종료)?',end='')
    s = input(); # 문자열 s 를 입력받는다
    if s=='0 0 0': break # 문자열 s 가 0 0 0 이라면 종료되도록 하고 아니라면 아래 수행
    print(calculator2(s)) # 계산된 값을 반환한다
'''
리뷰: 우선 연산자와 2개의 피연산자를 '인자로' 즉 매개변수로 받아와 사칙 연산을 수행해야 하는것이 요구사항이기에
두번째 eval 함수를 이용한 방법은 요구사항을 충족하지 못한다 생각된다. 파이썬 내에서는 공백을 기준으로 여러 변수를 입력
받을 때 기본 default input을 받을 때 문자 형으로 받게 된다. 그렇기에 수식의 계산을 위해 함수로 매개변수를 줄때 
float(실수형)으로 형변환을 거친 뒤 계산에 들어갔다. (+,-,*,/) 네번에 거쳐 경우의 수를 나누는 것 외에 다른 방법이 
없었을까 아쉬웠습니다. 
'''
