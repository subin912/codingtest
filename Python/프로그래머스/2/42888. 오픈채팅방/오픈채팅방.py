def solution(record):
    #1.아이디 일단 다 모으자
    answer = []
    nick={}
    for i in record:
        words = i.split()
        if words[0] == 'Enter' or words[0] == 'Change':
            nick[words[1]] = words[2] #id명이 key값으로 마지막 닉네임만 남게함!
            
    #2. 최종닉네임으로 메시지 만들기
    for i in record:
        words = i.split()
        if words[0] == 'Enter':
            answer.append(nick[words[1]] + '님이 들어왔습니다.')
        elif words[0] == 'Leave':
            answer.append(nick[words[1]] + '님이 나갔습니다.')
            
    return answer