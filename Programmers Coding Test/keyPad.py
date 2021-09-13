


def solution(numbers, hand):
    answer = ''
    keyPad = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}
    l = '*'
    r = '#'
    for i in range(len(numbers)):

        target = numbers[i]
        if target in [1,4,7,10]:
            answer+='L'
            l = target
        elif target in [3,6,9,12]:
            answer+='R'
            r = target
        else: # 2,5,8,0 인 경우
            x,y = keyPad[target]
            lx,ly = keyPad[l]
            rx,ry = keyPad[r]
            distl = abs(x-lx)+abs(y-ly)
            distr = abs(x-rx)+abs(y-ry)
            if distl > distr: # 왼손 거리가 더 멀다면 R
                answer+='R'
                r = target # 오른손을 키패드로 옮긴다
            elif distr > distl: # 오른손 거리가 더 멀다면 L
                answer+='L'
                l = target # 왼손을 키패드로 옮긴다
            else: # 서로 같다면
                if hand == 'left':
                    answer+='L'
                    l = target
                else:
                    answer+='R'
                    r = target
    return answer

numbers=[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
print(solution(numbers,'right'))

