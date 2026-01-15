# 피보나치수 가장 간단 방법 시간복잡도 O(n) : 반복문, 변수2개
a = 0
b = 1
n = int(input())

for _ in range(0,n):
    a , b = b, a+b
print(a)

# 메모이제이션 배열 사용방법 시간복잡도 O(n)
n = int(input())
p = [0]*46

for i in range(0,n+1):
    if i == 0:
        p[0] = 0
    elif i == 1:
        p[1] = 1
    else:
        p[i] = p[i-2] + p[i-1]
        
print(p[n])	

#더 깔끔히 방법
n = int(input())
p = [0] * 46
p[1] = 1

for i in range(2, n+1):
    p[i] = p[i-1] + p[i-2]

print(p[n])
