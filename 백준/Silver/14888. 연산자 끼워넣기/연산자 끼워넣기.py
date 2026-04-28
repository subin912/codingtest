n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))  # + - * /

mx, mn = -1e9, 1e9

def dfs(i, val):
    global mx, mn
    
    if i == n:
        mx = max(mx, val)
        mn = min(mn, val)
        return
    
    for j in range(4):
        if ops[j]:
            ops[j] -= 1
            
            if j == 0: dfs(i+1, val + nums[i])
            elif j == 1: dfs(i+1, val - nums[i])
            elif j == 2: dfs(i+1, val * nums[i])
            else:
                dfs(i+1, -(-val//nums[i]) if val < 0 else val//nums[i])
            
            ops[j] += 1

dfs(1, nums[0])

print(int(mx))
print(int(mn))