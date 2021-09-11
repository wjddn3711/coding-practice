import sys
input = sys.stdin.readline
target = input().rstrip('\n')
result = [] # 초기값
for i in range(len(target)):
    result.append(target[i:]) # 하나씩 슬라이싱하여 리스트에 저장
result.sort() # 자동으로 사전순으로 정렬됨
[print(result[i]) for i in range(len(result))]

