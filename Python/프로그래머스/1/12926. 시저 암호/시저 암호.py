#11:43
def solution(s, n):
    answer = '' #문자열로 나와야하기에 리스트 []로 정의안하는거!
    #이걸 n번 반복
    for i in range(len(s)):
    #소문자면 소문자 다음 걸로
        if s[i] == " ": #공백이면 한칸 띄워야함
            answer += s[i]
        
        elif s[i] == s[i].lower():
            answer += chr((ord(s[i]) - ord('a') + n) % 26+ ord('a'))
    
    #대문자면 대문자 다음 걸로
        else:# s[i] == s[i].upper():
            answer += chr((ord(s[i]) - ord('A') + n) % 26+ ord('A'))

    return answer