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
