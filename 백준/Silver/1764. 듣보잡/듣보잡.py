# N,M 입력 받기
n,m = map(int, input().split())
#중복되는 사람 없음
#N개의 줄에 걸쳐 듣도 못한 사람의 이름

#듣지못하는 n명 이름 저장
no_listen = set() #저장소 set으로 만들기, 중복없으니까

for _ in range(n):
    name = input().strip()  # strip(): 줄바꿈 문자 제거하고 들어오도록
    no_listen.add(name)

#보지못하는 m명 이름 보면서 - set안에 있으면 result에 추가
result = [] #둘 다 해당되는 사람들 모아둘 리스트
for _ in range(m):
    name = input().strip()
    if name in no_listen: 
        result.append(name)

result.sort()

print(len(result))
for name in result:
    print(name)