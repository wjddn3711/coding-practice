s = "abcd"

def solution(s):
    if len(s)%2==1: #홀수인 경우
        answer = s[len(s)//2]
    else: # 짝수인 경우
        answer = s[len(s)//2-1:len(s)//2+1]
    return answer

print(solution(s))