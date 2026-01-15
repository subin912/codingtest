T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    # 0층 계산
    people = [i for i in range(n + 1)]

    # 1층부터 k층까지 계산
    for _ in range(k):
        for i in range(1, n + 1):
            people[i] += people[i - 1]

    print(people[n])