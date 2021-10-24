# 1   2   3   4   5   6   7   8   9   0
# 2	  5	  5	  4	  5	  6	  3	  7	  6	  6

testCase = int(input())
for _ in range(testCase):
    n = int(input())
    # 성냥개비가 최소가 되기 위해서는 n이 10을 초과할때, 8로 채우고 나머지 성냥으로 조합하는 것이 최소가 된다
    maxStick = '7'*(n%2)+'1'*(n//2-(n%2))
    # 성냥개비가 7개 미만인경우 2-6개인 경우
    '''
    2 : 1
    3 : 7
    4 : 4
    5 : 2
    6 : 6
    '''
    underCase=[0, 0, 1, 7, 4, 2, 6, 8, 10, 18, 22]
    if n<=10:
        print(underCase[n],maxStick)
        continue
    '''
    나머지 1 부터 6 인 경우
    1 : minStick 의 가장 앞자리를 제거하고, 8로 만들수 있는 최소값 10
    2 : minStick 의 가장 앞자리를 제거하고, 9로 만들수 있는 최소값 18
    3 : minStick 의 가장 앞두자리를 제거하고, 17으로 만들 수 있는 최소값 200
    4 : minStick 의 가장 앞자리를 제거하고, 11로 만들 수 있는 최소값 20
    5 : minStick 의 가장 앞자리를 제거하고, 12로 만들 수 있는 최소값 28
    6 : minStick 의 가장 앞자리를 제거하고, 13으로 만들 수 있는 최소값 68
    '''
    minStick = '8'*(n//7) # 우선 7로 나누어떨어지지 않을때 까지 8로 채워준다
    rest = n%7
    if rest==1: minStick='10'+minStick[1:]
    elif rest==2: minStick='18'+minStick[1:]
    elif rest==3: minStick='200'+minStick[2:]
    elif rest==4: minStick='20'+minStick[1:]
    elif rest==5: minStick='28'+minStick[1:]
    elif rest==6: minStick='68'+minStick[1:]
    print(minStick,maxStick)


