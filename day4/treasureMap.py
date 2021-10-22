arr1 =[9, 20, 28, 18, 11]
arr2 =[30, 1, 21, 17, 28]

def toTwo(num,n):
    digit = ''
    while num > 0 :
        div, mod = divmod(num,2)
        digit+= str(mod)
        num=num//2
    digit =digit[::-1].zfill(n) # 순서를 반전시키고 0으로 채운다
    return digit

def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        update = ''
        arr1[i] = toTwo(arr1[i],n)
        for j in range(len(arr1[i])):
            if arr1[i][j] == '1': update+='#'
            else: update+=' '
        answer.append(update)
    for i in range(len(arr2)):
        arr2[i] = toTwo(arr2[i],n)
        answer[i] = list(answer[i])
        for j in range(len(arr2[i])):
            if answer[i][j] ==' ': # 아직 안채워진 맵이라면
                if arr2[i][j] == '1':
                    answer[i][j]='#'
                # arr2가 1이라면 공백을 #으로 바꿔준다
        answer[i] = ''.join(answer[i])
    return answer

print(solution(5,arr1,arr2))