def solution(s, n):
    answer = ''
    for i in range(len(s)):
        #공백
        if s[i] == ' ':
            answer += s[i]
        elif s[i].islower():
            answer += str(chr(((ord(s[i])-ord('a')+n)) %26 + ord('a')))
        elif s[i].isupper():
            answer += str(chr(((ord(s[i])-ord('A')+n)) %26 + ord('A')))
    return answer