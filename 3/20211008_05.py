numbers = [2,7]
def solution(numbers):
    answer = []
    for target in numbers: # numbers에 저장된 타겟 값을 받아온다
        bit = bin(target).lstrip('0b')
        # bit값으로 변환한 target을 변환한다. 기본적으로 '0bXX'가 되는데 앞의 0b를 빼준다
        i = 1
        bzc = bit.count('0')
        boc = bit.count('1')
        while True:
            comp = bin(target+i).lstrip('0b') # 비교할 대상
            czc = comp.count('0') # comp의 1의 개수와 0의 개수
            coc = comp.count('1')
            if abs(boc-coc) + abs(bzc-czc) <=2: # 1의 개수의 차 + 0의 개수의 차가 2이하일 때 탈출한다
                break
            # 아니라면 i 증가
            i+=1
        answer.append(target+i) # 타겟 + i는 다른 지점 2개 이하이면서 제일 작은수
    return answer

'''
리뷰: 처음으로 bin 이라는 함수에 대해 알게 되었다. 비트를 다루는 일이 흔하지 않다보니 좋은 경험이 되었던것 같다. 문제의 난점이라고 생각되는 점이 두가지 
있는데 첫번째 2진수로 변환이며 두번째는 비트가 다른 지점의 판단이였다. 처음에는 Counter 를 떠올려 딕셔너리 형태로 만들어 values들의 차를 이용하여 구현
하려고 하였지만 bin을 이용한 값은 앞의 0을 무시하고 1부터 반환하기에 7인 경우 {'1':3} 의 형태로 나와 0의 값을 비교할 수 없었다. 그래서 비트 값임을 
이용하여 두가지 값밖에 존재하지 않기때문에 각수를 이진수로 변환한뒤 1의 개수와 0의 개수를 count 메서드를 활용하여 개수를 구하였다. 생소한 문제이지만 bin
이라는 함수에 대해 알수 있어 뜻깊었다. 
'''

