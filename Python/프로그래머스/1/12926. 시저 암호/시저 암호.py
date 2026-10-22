#옆으로 밀어야하는데 다시 돌아와야함 26개
def solution(s, n):
    low='abcdefghijklmnopqrstuvwxyz'
    upp='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = ''
    #print(25%25)
    #print(low.index('z'))
    for i in range(len(s)):
        #공백이면 공백처리
        if s[i] == " ":
            answer += s[i]
        #소문자
        elif s[i].islower():
            answer += low[(low.index(s[i]) + n) % 26]
    
        #대문자
        elif s[i].isupper():
            answer += upp[(upp.index(s[i]) + n) % 26]
            
    return answer