# 테스트 케이스 입력
for t in range(int(input())):
    # 금광 정보 입력
    n, m = map(int, input().split())
    ar = list(map(int,input().split()))
    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    for i in range(0,n*m,m):
        dp.append(ar[i:i+m])
    # 다이나믹 프로그래밍 진행
    for j in range(1,m): # 첫번째 열은 시작열이기 때문에 생략하고 진행
        for i in range(n): # n개의 j열 i행의 값들중 최대값을 더하여 준다
            # 왼쪽 위에서 오는 경우
            if i==0: left_up=0 # 왼쪽 위가 없는 경우 0으로 초기화
            else: left_up=dp[i-1][j-1]
            # 왼쪽 에서 오는 경우
            left = dp[i][j-1]
            # 왼쪽 아래에서 오는 경우
            if i==n-1: left_down=0 # 왼쪽 아래가 없는 경우 0으로 초기화
            else: left_down=dp[i+1][j-1]
            dp[i][j]=max(left,left_down,left_up)+dp[i][j] # 위 세가지 경우중 가장 큰값
    # dp 초기화 이후 m-1번째 열에서 최대값을 구해준다
    result = dp[0][m-1] # dp 리스트의 우측 상단의 값을 max로 초기화
    for i in range(1,n):
        result=max(result,dp[i][m-1])
    print(result)