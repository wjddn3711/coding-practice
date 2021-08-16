def solution(record):
    command=[]
    id = []
    answer = []
    idDict ={}
    for i in range(len(record)):
        command.append(record[i].split()[0])
        id.append(record[i].split()[1])
        if command[i]=='Enter' or command[i]=='Change':
            idDict[id[i]] = record[i].split()[2]

    for i in range(len(record)):
        if command[i]=='Enter':
            answer.append('{}님이 들어왔습니다.'.format(idDict[id[i]]))
        elif command[i]=='Leave':
            answer.append('{}님이 나갔습니다.'.format(idDict[id[i]])) # idDict에 저장된 닉네임 출력
        else:
            continue
    return answer


record =["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))