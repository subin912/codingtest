# def solution(phone_book):
#     # 1. 정렬하면 접두어 관계인 것끼리 이웃하게 됨. ex) ["12", "123", "567"]
#     phone_book.sort()
    
#     # 2. 1번 인덱스부터 시작해서 바로 앞번호(i-1)와 비교
#     for i in range(len(phone_book)):
#             # 바로 뒷번호가 앞번호로 시작하는지 체크
#             if phone_book[i].startswith(phone_book[i-1]):
#                 return False # 하나라도 찾으면 즉시 종료
#     # for문 다 돌 때까지 False 안나왔다면 접두어가 없는 것        
#     return True #파이썬에서 첫글자 대문자 써야함 (True, False)


######### 해시로 풀기
def solution(phone_book) :
    # 1. 모든 번호 딕셔너리(해시 맵)에 담기
    hash_map = {}
    for number in phone_book:
        hash_map[number] = True  # 번호를 이름표(Key)로 사용

    # 2. 각 번호마다 접두어 하나씩 검사 ( 각 번호를 하나씩 꺼내서 검사)
    for number in phone_book:
        exp = ""
        # 번호의 글자를 하나씩 더해가며 접두어를 만듦
        # "123"일 때 "1", "12"까지만 생성(마지막 글자 제외: [:-1]) <- 마지막 글자 제외안하면 자기 자신 마주침
        for char in number[:-1]:
            exp = exp + char
            # 3. 만들어진 조각(exp)이 해시 맵 즉 이름표에 있는지 확인
            if exp in hash_map:
                return False # 누군가의 번호가 내 접두어라는 뜻!
    # 모든 번호를 다 검사했는데 걸리는 게 없다면 True
    return True

