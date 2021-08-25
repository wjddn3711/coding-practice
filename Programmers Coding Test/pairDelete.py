from collections import deque
s = 'cscs'

def solution(s):
    record =[]
    answer =-1
    for word in s:
        if len(record)==0:
            record.append(word)
        elif record[-1]==word:
            record.pop()
        elif record[-1]!= word:
            record.append(word)
    if len(record)==0:
        answer+=2
    else:
        answer+=1
    return answer

print(solution(s))