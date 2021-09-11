from string import ascii_lowercase as asl
from string import ascii_uppercase as asu
import sys
input = sys.stdin.readline
# rot13 암호화된 새로운 알파뱃 리스트
newAlphaLow = list(asl)[13:]+list(asl)[:13]
newAlphaUp = list(asu)[13:]+list(asu)[:13]

target = input().rstrip('\n')
for char in target:
    if char.islower():
        # list(asl).index(char) 는 본래 알파뱃 순서
        print(newAlphaLow[list(asl).index(char)],end='')
    elif char.isupper(): # 대문자라면
        print(newAlphaUp[list(asu).index(char)],end='')
    else: # 숫자나 공백인 경우 바로 출력
        print(char,end='')
