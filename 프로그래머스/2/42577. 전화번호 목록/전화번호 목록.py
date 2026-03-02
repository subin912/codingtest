def solution(phone_book):
    # 1. 정렬하면 접두어 관계인 것끼리 이웃하게 됨. ex) ["12", "123", "567"]
    phone_book.sort()
    
    # 2. 1번 인덱스부터 시작해서 바로 앞번호(i-1)와 비교
    for i in range(len(phone_book)):
            # 바로 뒷번호가 앞번호로 시작하는지 체크
            if phone_book[i].startswith(phone_book[i-1]):
                return False # 하나라도 찾으면 즉시 종료
    # for문 다 돌 때까지 False 안나왔다면 접두어가 없는 것        
    return True #파이썬에서 첫글자 대문자 써야함 (True, False)