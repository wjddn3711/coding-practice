# '(' 와 ')' 로만 이루어진 문자열이 있을 경우, '(' 의 개수와 ')' 의 개수가 같다면 이를 균형잡힌 괄호 문자열이라고 부릅니다.
# 그리고 여기에 '('와 ')'의 괄호의 짝도 모두 맞을 경우에는 이를 올바른 괄호 문자열이라고 부릅니다.
# 예를 들어, "(()))("와 같은 문자열은 "균형잡힌 괄호 문자열" 이지만 "올바른 괄호 문자열"은 아닙니다.
# 반면에 "(())()"와 같은 문자열은 "균형잡힌 괄호 문자열" 이면서 동시에 "올바른 괄호 문자열" 입니다.
# '(' 와 ')' 로만 이루어진 문자열 w가 "균형잡힌 괄호 문자열" 이라면 다음과 같은 과정을 통해 "올바른 괄호 문자열"로 변환할 수 있습니다.
p = "))(("
def balanced(p):  # ( 의 개수가 ) 개수와 같은지 판단, u v 를 나눌때 밸런스 있게 나누도록하는 함수
    if p.count('(') == p.count(')'):
        return True
    else:
        return False

def uvSplit(p): # 2번째 인덱스 부터 시작하여 만약 밸런스있다면 u 와 v 로 나눈다
    for i in range(2, len(p)+1):
        if balanced(p[:i]) and balanced(p[i:]):
            return p[:i], p[i:]

def correct(p): # 나눠진 u 가 () 의 형태라면 True 를 반환 하도록
    l, r = 0, 0
    for s in p:
        if s == '(':
            l += 1
        else: # ) 라면 m +1
            r += 1
        if r > l: return False
    return True

def solution(p):
    if p == '': # p가 공백이라면 그대로 p 를 반환하도록 한다
        return p
    u, v= uvSplit(p)
    if correct(u): # 올바르게 괄호가 나눠졌다면
        return u + solution(v) # v 부분을 재귀적으로 호출하여 올바르게 바꾼다
    else:
        return "("+solution(v)+")"+u[1:-1].replace('(','temp').replace(')','(').replace('temp',')')

print(solution(p))