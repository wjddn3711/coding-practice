def solution(str1, str2):
    answer = 0
    a,b =sets(str1,str2) # str1 집합을 a 로, str2는 b로 지정
    print('a: ',a)
    print('b: ',b)
    intersec= set(a)&set(b) # 교집합
    union= set(a)|set(b) # 합집합
    if 0 in [len(intersec),len(union)] : return 65536
    J = len(intersec)/len(union)
    answer = int(65536*J)
    print(answer)
    return answer

def sets(str1, str2):
    A = []
    B = []
    # 특수 문자는 올 수 없도록 반복을 돌려 특수문자를 문자열에서 제거해준다
    # i=0
    # while True:
    #     if i==len(str1):break # 만약 i 가 인덱스 범위를 넘어가면 탈출
    #     if str1[i].isalpha(): #만약 문자라면 다음 자리로 넘어감
    #         i+=1
    #         continue
    #     # 문자가 아니라면 아래 수행
    #     if i+1==len(str1): # 가장 끝이 문자가 아니라면 이전까지 슬라이싱
    #         str1=str1[:i]
    #     else: # 가장 끝이 아니라면 뒤에 문자와 합침
    #         str1=str1[:i]+str1[i+1:]
    # i=0
    # while True:
    #     if i==len(str2):break # 만약 i 가 인덱스 범위를 넘어가면 탈출
    #     if str2[i].isalpha(): #만약 문자라면 다음 자리로 넘어감
    #         i+=1
    #         continue
    #     # 문자가 아니라면 아래 수행
    #     if i+1==len(str2): # 가장 끝이 문자가 아니라면 이전까지 슬라이싱
    #         str2=str2[:i]
    #     else: # 가장 끝이 아니라면 뒤에 문자와 합침
    #         str2=str2[:i]+str2[i+1:]

    # 두개씩 슬라이스하여 저장한다
    for k in range(len(str1)):
        isChar = True
        # 각 문자열의 길이만큼 반복하여 집합안에 넣는다
        if k+1==len(str1):break # 만약 길이를 초과한다면 슬라이싱 중단
        for char in str1[k:k+2]:
            if not char.isalpha():
                isChar=False # 만약 문자가 아니라면 무시
                break
        if isChar: A.append(str1[k:k+2].upper()) # 두 문자씩 끊어서 A 집합에 저장한다

    for j in range(len(str2)):
        isChar = True
        if j+1==len(str2):break
        for char in str2[j:j+2]:
            if not char.isalpha():
                isChar=False # 만약 문자가 아니라면 무시
                break
        if isChar: B.append(str2[j:j+2].upper()) # 대소문자를 가리지 않기에 대문자로 통일한다
    return A,B

str1 = "E=M*C^2"
str2 = "e=m*c^2"

solution(str1,str2)
