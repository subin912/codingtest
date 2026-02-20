# 피보나치 수
import sys
sys.setrecursionlimit(10**7)  # 재귀 깊이 제한 완화

# = [0]* 101   # 0 ~ 100까지 커버
n = int(input())

p = [0]*(n+1)

def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if p[n] == 0: #재귀를 dp(동적 계획법)으로 만들어줌
        p[n] = fib(n-1) + fib(n-2)
    return p[n]

print(fib(n))