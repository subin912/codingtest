def solution(arr):
    result = []
    for i in range(0,len(arr)):
        if i == 0:
            result.append(arr[i])
        elif arr[i] != arr[i-1]:
            result.append(arr[i])
        else:
            pass
    return result

## 좀 더 깔끔풀이
def solution(arr):
    result = [arr[0]] #리스트로 시작
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            result.append(arr[i])
    return result
