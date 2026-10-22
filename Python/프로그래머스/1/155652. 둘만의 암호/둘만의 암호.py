def solution(s, skip, index):
    answer = ''

    for i in range(len(s)):
        cnt = 0
        j = 0
        while cnt <index:
            j += 1
            k = chr((ord(s[i]) - ord('a') + j) % 26 + ord('a'))
            if str(k) not in skip:
                cnt += 1
        answer += k
    return answer