from string import ascii_lowercase
import sys
input = sys.stdin.readline
alphaList = list(ascii_lowercase) # 소문자 알파벳을 저장할 리스트
target = input().strip() # 타겟 입력
result = [-1]*26 # 결과값 초기화
stack = []
# 중복을 없애준다. set을 사용하면 순서가 이상해져서 스택을 이용
for i in range(len(target)):
    if target[i] in stack: # 만약 문자가 스택안에 존재한다면 무시
        continue
    else:
        stack.append(target[i])
        result[alphaList.index(target[i])]=i
    # alphaList.index(target[i]) 는 타겟알파벳의 알파뱃 순열상 위치
    # 그리고 그 위치에 타겟 문자의 인덱스를 저장한다
print(*result)
