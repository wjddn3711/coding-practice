new_id = "...!@BaT#*..y.abcdefghijklm"

def solution(new_id):
    # answer = new_id.lower() # 1단계 대문자를 소문자로
    answer = ''
    for char in new_id.lower():
        if char.isalnum(): # 문자, 숫자라면 패스
            answer+=char
        elif char in '-_.':
            answer+=char
    # .. 제거
    while '..' in answer:
        answer = answer.replace('..','.')
    # . 앞 뒤 제거
    answer = answer[1:] if answer[0]=='.' and len(answer)>1 else answer
    answer = answer[:-1] if answer[-1]=='.'  else answer

    answer = 'a' if len(answer)==0 else answer
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 2 자 이하라면 3이 될때까지 마지막 문자를 붙임
    while len(answer) < 3:
        answer+=answer[-1]

    return answer

solution(new_id)