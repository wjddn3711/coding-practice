n = 125
stack = []
while n > 0: # n이 더이상 나누어 떨어지지 않을때까지
    # 3진법으로 바꿀때 append 를 써서 나머지를 저장하면 자동으로 역순으로 저장된다
    stack.append(n%3) # 스택에 나머지를 저장한다
    n=n//3 # 3으로 나누어준다
print(stack)

def solution(n):
    answer = ''
    while n > 0: # n이 더이상 나누어 떨어지지 않을때까지
        # 3진법으로 바꿀때 append 를 써서 나머지를 저장하면 자동으로 역순으로 저장된다
        # stack.append(n%3) # 스택에 나머지를 저장한다
        # n=n//3 # 3으로 나누어준다
        n, mod = divmod(n,3)
        answer += str(mod)
    answer = int(answer,3)
    #
    # print(stack)
    # for i in range(-1, (len(stack)*-1)-1,-1):#뒤에서 부터 -1씩 증가하면서
    #     # i는 -1 ~ -n 까지이다 10진수로 만들기 위해서는 i*-1 한뒤 3의i승을 더해주면된다
    #     if stack[i]==0: continue # 만약 스택값이 0이라면 계산없이 다음으로
    #     x = (i*-1)-1
    #     answer += (3**x)*stack[i] # 3의 i승 으로 계산
    return answer

print(solution(125))