def solution(n):
    total = 0
    for x in range(1,n+1):
        if n % x == 0:
            total = total + x
    return total