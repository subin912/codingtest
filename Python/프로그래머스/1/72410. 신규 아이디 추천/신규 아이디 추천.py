def solution(new_id):
    #print(new_id.lower())
    #1단계
    s = new_id.lower()
    #2단계 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한거 제거
    t = ''
    for i in range(len(s)):
        if s[i].isalnum() or s[i] in '-_.':
            t += s[i]       
    #3단계 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    while '..' in t:
        t = t.replace('..','.')
    #4단계 마침표(.)가 처음이나 끝에 위치한다면 제거
    t = t.strip('.')
    #5단계 빈문자열이면 "a"넣기
    if t =='':
        t = "a"
    #6단계 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    #만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
    if len(t) >= 16:
        t = t[:15].rstrip('.')
    #7단계
    if len(t) <=2:
        while len(t) < 3: # == 은 길이가 3일동안 반복이야!! <은 3되기전까지 반복
            t = t + t[-1]
    print(t)
    return t