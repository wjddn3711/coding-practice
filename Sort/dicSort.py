n = int(input())
dic = {}
key = [] # 초기 단어 생성
value = [] # 초기 단어 길이 생성
for i in range(n):
    key =input()# key는 단어
    value =len(key) # key의 길이만큼 추가
    dic[key]=value # 딕셔너리 생성
result = sorted(dic.items(), key = lambda x:(x[1],x[0])) # 단어의 길이를 우선으로 정렬후 같으면 사전순으로 출력
for key, value in result: # result 에는 튜플 형식으로 값이 담긴다
    print(key) # 정렬된 result에서 키값인 단어를 출력시킨다