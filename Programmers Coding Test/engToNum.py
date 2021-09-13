s ="one4seveneight"

def solution(s):
    eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for key in eng:
        if key in s:
            s = s.replace(key,str(eng.index(key)))
    answer = int(s)
    return answer

S =solution(s)
print(S)
