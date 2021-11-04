from collections import Counter
n = int(input()) # 수들의 수
numbers = [int(input()) for _ in range(n)] # n개의 수를 리스트에 저장
# 산술평균
print(round(sum(numbers)/n)) # 소수점 1의 자리에서 반올림한 평균값
# 중앙값
numbers.sort() # 수들을 오름차순으로 정렬
print(numbers[n//2]) # 오름차순으로 정렬된 리스트의 중앙값
# 최빈값
countNum = Counter(numbers) # 키:수, 벨류:빈도수 형식의 딕셔너리 생성
maxFreqNum = max(countNum.values()) # 빈도수들중 가장 큰값
maxFreqCnt = list(countNum.values()).count(maxFreqNum) # 최대빈도수를 가진 값이 많은지 체크
if maxFreqCnt >1: # 최대빈도수를 가진 값이 1보다 크다면
    isSecond = False
    for key in sorted(countNum.keys()): # 오름차순으로 정렬된 키값들
        if isSecond: # 만약 두번째로 작은 최대빈도수 값이라면 그 수를 출력하고 반복 종료
            print(key)
            break
        if countNum[key] == maxFreqNum: # 해당 키의 벨류값이 최대 빈도수라면 isSecond를 True로 바꾼다
            isSecond = True
else: # 최대빈도수를 가진 값이 하나라면 그 값만 찾고 반복 종료
    for key in countNum.keys():
        if countNum[key]==maxFreqNum:
            print(key)
            break
# 범위
print(numbers[-1]-numbers[0]) # 최대값과 최솟값의 차이

