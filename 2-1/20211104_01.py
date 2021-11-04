n = int(input()) # 회원수
userList = [] # 회원 리스트
for i in range(n):
    age, name = input().split() # 공백을 기준으로 나이와 이름을 받아온다
    userList.append([int(age),name, i]) # 0번째 인덱스: 나이, 1번째 인덱스: 이름으로 저장한다, 2: 회원가입 순서
userList.sort(key =lambda x:(x[0], x[2])) # 0번째인 나이를 기준으로 오름차순, 같다면 회원가입순서로 정렬
for age, name, id in userList:
    print('{} {}'.format(age, name)) # 형식에 맞게 출력

