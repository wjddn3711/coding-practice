# # 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
# #
# # Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
# #
# # X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.
# import sys
# n = int(sys.stdin.readline())
# ar = list(map(int,sys.stdin.readline().split()))
# dicAr = sorted({key:0 for key in ar}) # ar에 담긴 값들을 하나씩 담아주고 정렬한다
# for i in range(n):
#     if i==n-1:
#         print(dicAr.index(ar[i]))
#     else:
#         print(dicAr.index(ar[i]),end=' ')


n=int(input())
ar=list(map(int,input().split()))
dicAr = sorted({key:0 for key in ar}) # ar에 담긴 값들을 하나씩 담아주고 정렬한다
arDict={i:v for v,i in enumerate(dicAr)}
for i in ar:
    print(arDict[i],end =' ')