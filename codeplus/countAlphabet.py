from collections import Counter
from string import ascii_lowercase
import sys
input = sys.stdin.readline
target = input().strip()
alphaList = list(ascii_lowercase) #(a~z 까지의 알파벳)
result = [0]*26 # 알파뱃 초기화
cntTarget = Counter(target) #타겟의 각 알파뱃 개수
# print(cntTarget)
for key in cntTarget.keys(): #알파뱃 개수
    result[alphaList.index(key)]=cntTarget[key]
    # alphaList.index(key) 는 타겟 알파뱃의 기존 알파뱃 순서에서의 인덱스
    # cntTarget[key] 는 기존 알파뱃 순서에 타겟 알파뱃이 등장한 횟수를 저장
print(*result)