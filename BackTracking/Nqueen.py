import sys
input = sys.stdin.readline
# cnt = 0
# n = int(input()) # 맵의 크기
# col = [0 for _ in range(n)] # 퀸의 위치를 저장할 리스트
# def isCorrect(i):
#     for x in range(i):
#         if col[i] == col[x] or abs(col[i]-col[x]) == i-x:
#         # 만약 같은 열에 위치하거나 대각선에 위치한다면
#             return False # 올바른 위치가 아니다
#     return True
#
# def nQueens(i):
#     global cnt
#     if i == n:  # 만약 퀸의 개수가 n 개라면 탈출하면서 경우의 수를 반환
#         cnt += 1
#     else:
#         for j in range(n):
#             col[i] = j  # col[1]=1~n 까지 1,1~1,n 까지 반복
#             if isCorrect(i):
#                 nQueens(i + 1)
# nQueens(0)
# print(cnt)
cnt =0
def Nqueens(col):
    # 차례대로 0,1,2 ~ n 에 해당하는 행을 입력 받아 만약 최대 깊이까지 만족하는 행이 n의 길이일때 cnt 를 늘려주도록 한다
    global cnt
    if len(col)==n: # 길이가 n 일 때, 경우의 수 카운트를 1증가 시킨다
        cnt +=1
    else:
        for i in range(n):  # i 는 새로 들어올 행 인덱스
            if i in col: # 만약 i == ar[x] 라고 할때 같은 행에 퀸이 존재해서는 안되기에 무시하게 한다
                continue
            for j in range(len(col)):
                if abs(i-col[j]) == len(col) - j:  # 대각선에 위치한다면
                    break  # 탈출
            else: # 대각선에 위치하지 않는다면
                col.append(i) # 리스트에 i 를 삽입
                Nqueens(col) # 재귀호출하여 새로운 리스트에 대하여 퀸의 위치 설정
                print(col)
                col.pop()
n = int(input())
for i in range(n):
    Nqueens([i])

print(cnt)




