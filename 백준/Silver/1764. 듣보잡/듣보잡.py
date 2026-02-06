#집합 A = “듣도 못한 사람들”
#집합 B = “보도 못한 사람들”
#A ∩ B (교집합) 구하는 문제
#------------------------------
#no_see는 따로 폴더 안만들고, 
#no_listen 보고 겹치는 애만 result에 추가
#------------------------------

# N,M 입력 받기
n,m = map(int, input().split())

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

#------------------------------------------
#a = {input().strip() for _ in range(n)}
#b = {input().strip() for _ in range(m)}

#ans = sorted(a & b)
