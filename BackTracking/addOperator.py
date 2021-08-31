import sys
input = sys.stdin.readline
n = int(input()) # 연산할 숫자의 개수
numbers = list(map(int, input().split())) # 연산할 수
opList = list(map(int, input().split())) # 연산자의 개수를 저장할 리스트

maxVal = -sys.maxsize
minVal = sys.maxsize



def solve(num,index,add,minus,multi,div):
    global maxVal
    global minVal
    if index==n-1: # 만약 최대깊이까지 도달 했다면

        maxVal = max(num,maxVal)
        minVal = min(num,minVal)
        return

    if add:  # 만약 + 연산자가 있다면
        solve((num + numbers[index+1]), index + 1, add-1, minus, multi, div)
    if minus:  # 만약 - 연산자라면
        solve((num - numbers[index+1]), index + 1, add, minus-1, multi, div)
    if multi:
        solve((num * numbers[index+1]), index + 1, add, minus, multi-1, div)
    if div:
        solve(int(num / numbers[index+1]), index + 1, add, minus, multi, div-1)

num=numbers[0] # numbers의 0 부터 시작
solve(num, 0, opList[0], opList[1], opList[2], opList[3])
print(maxVal)
print(minVal)



