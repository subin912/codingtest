def solution(n):
    answer = ''
    for i in range(1,n+1):
        if i % 2 == 0:
            answer = answer + '박'
        else:
            answer = answer + '수'
    return answer

#10^4 는 반복문 1번은 괜찮다. 2번은 안됨?