from string import ascii_lowercase, ascii_uppercase

lower = list(ascii_lowercase)  # ['a' ... 'z']
upper = list(ascii_uppercase)  # ['A' ... 'Z']

def solution(s, n):
    result = ""

    for ch in s:
        if ch == " ":
            result += " "  # 공백은 그대로

        elif ch in lower:  # 소문자
            i = lower.index(ch)
            result += lower[(i + n) % 26]

        elif ch in upper:  # 대문자
            i = upper.index(ch)
            result += upper[(i + n) % 26]

    return result


# def solution(s, n):
#     answer = ''
#     low_ap = list(ascii_lowercase)
#     upp_ap = list(ascii_uppercase)
    
#     if s in low_ap:
#         i = low_ap.index(s)
#         new_i = (i + n) % 26 #알파벳 총 개수 26개
#         print(low_ap[new_i])
#     else:
#         i = upp_ap.index(s)
#         new_i = (i + n) % 26 #알파벳 총 개수 26개
#         print(upp_ap[new_i])
#     return answer


# #알파벳이 소문자, 대문자, 공백