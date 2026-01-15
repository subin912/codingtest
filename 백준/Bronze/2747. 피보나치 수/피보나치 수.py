a = 0
b = 1
n = int(input())

for _ in range(0,n):
    a , b = b, a+b
print(a)
    