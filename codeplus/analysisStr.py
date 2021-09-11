from string import ascii_lowercase,ascii_uppercase
import sys
input = sys.stdin.readline
while True:
    target = input().rstrip('\n') # 타겟을 입력받는다
    if not target:
        break
    else:
        lower = 0
        upper = 0
        number = 0
        space = 0
        for char in target:
            if char == ' ': # 공백이라면
                space+=1
            elif char.isupper(): # 만약 대문자라면
                upper+=1
            elif char.islower(): # 소문자라면
                lower+=1
            else: # 숫자라면
                number+=1
        print(lower,upper,number,space)



analysis(4)