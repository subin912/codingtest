import sys

n = int(sys.stdin.readline())

if n < 2:
    print(1)
else:
    # dp[i]는 n=i일 때의 호출 횟수
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n + 1):
        # i를 호출할 때: (i-2 호출 횟수) + (i-1 호출 횟수) + (자기 자신 1번)
        dp[i] = (dp[i-2] + dp[i-1] + 1) % 1000000007
    
    print(dp[n])