from collections import Counter
def solution(want, number, discount):
    answer = 0
    #dict에 담기
    dict={}
    for i in range(len(want)):
        dict[want[i]] = number[i]
    #슬라이딩 ㄱㄱ    
    for i in range(len(discount)-9):
        if dict == Counter(discount[i:i+10]):
            answer += 1
    return answer