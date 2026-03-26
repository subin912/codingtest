def solution(N, number):
    if N == number:
        return 1
    
    dp = [set() for _ in range(9)]  # 1~8 사용
    
    for i in range(1, 9):
        # 1. 이어붙인 숫자 (ex: 5 → 55 → 555)
        dp[i].add(int(str(N) * i))
        
        # 2. 사칙연산 조합
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i - j]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(x * y)
                    if y != 0:
                        dp[i].add(x // y)
        
        # 3. number 찾으면 바로 반환
        if number in dp[i]:
            return i
    
    return -1