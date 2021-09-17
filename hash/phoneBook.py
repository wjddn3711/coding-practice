phone_book = ["12","123","1235","567","88"]

def solution(phone_book):
    answer = True
    phone_book.sort() # sort 를 통해 정렬을 진행하면 접두어가 있을 시 비교되는 것의 옆에 위치한다
    # 즉 옆에 있는 것들 끼리 비교하며 만약 접두어 라면 false 가 되도록 한다
    print(list(zip(phone_book,phone_book[1:])))
    # [('12', '123'), ('123', '1235'), ('1235', '567'), ('567', '88')]
    # ["12","123","1235","567","88"]
    # ['123', '1235', '567', '88']
    for a,b in zip(phone_book,phone_book[1:]):
        if b.startswith(a): # b 가 a 로 시작한다면 true
            # startswith 기억하자!
            answer = False
    # flag = False
    # for numbers in phone_book:
    #     for others in phone_book:
    #         if numbers==others: continue # 만약 자신의 번호라면 건너뛴다
    #         elif numbers in others: # 해당 번호가 다른 번호에 있다면
    #             answer = False
    #             flag = True
    #             break
    #     if flag: break
    return answer
print(solution(phone_book))