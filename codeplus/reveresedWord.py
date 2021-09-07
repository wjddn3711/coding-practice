string = input()
re = '' # 괄호안 문자를 저장
no = '' # 괄호밖 문자를 저장
result = []
flag = False
for char in string:
    if char == '<':  # 만약 괄호의 시작이라면 괄호를 표시하기 위해 플래그를 참으로 바꾼다
        flag = True
        result.append(no)
        re += char
        no = ''
    elif char == '>':  # 괄호의 끝이라면 플래그를 거짓으로 바꾼다
        flag = False
        re += char
        result.append(re)
        re = ''  # re를 다시 공백으로 초기화
    elif flag:
        re += char
    else:  # 만약 괄호가 아니고 괄호안의 문자도 아니라면
        no += char
result.append(no)  # 태그가 세개 이상이라면 반복이 끝나고 따로 no 를 저장해준다
for strs in result:
    if '>' in strs:
        print(strs, end='')
    elif strs == '':
        continue
    elif ' ' in strs:
        ar = strs.split()  # 공백을 기준으로 나눈다
        for i in range(len(ar)):
            if i == len(ar)-1: # 마지막에는 공백이 없도록
                print(ar[i][::-1], end='')
            else:
                print(ar[i][::-1], end=' ')  # 문자열을 뒤에서 부터 출략
    else:
        print(strs[::-1],end='')

# else: # 문자열에 태그가 포함 되어있지 않다면
#     ar = string.split() # 공백을 기준으로 나눈다
#     for string in ar:
#         print(string[::-1], end=' ') # 문자열을 뒤에서 부터 출략
