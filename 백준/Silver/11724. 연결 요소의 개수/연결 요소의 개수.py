import sys
input = sys.stdin.readline

# 1. 대장(부모) 찾기 함수 
def find(parent, x):
    # 만약 x의 부모가 자기 자신이 아니라면, 아직 진짜 대표까지 안 올라간 상태라는 뜻
    if parent[x] != x:
        # 재귀적으로 부모의 부모를 계속 따라 올라가서 최종 대표를 찾는다.
        # 그리고 찾는 김에 parent[x]를 최종 대표로 바로 바꿔준다.
        parent[x] = find(parent, parent[x]) #경로압축해주는것 : 부모바꿔줘
    
    # 최종 대표(대장) 반환
    return parent[x]

# 2. 두 팀 합치기 함수
def union(parent, a, b):
    rootA = find(parent, a) # a가 속한 팀의 대표 찾기
    rootB = find(parent, b) # b가 속한 팀의 대표 찾기
    if rootA != rootB: # 대표가 다르면 서로 다른 팀이라는 뜻
        parent[rootB] = rootA # b팀의 대표를 a팀 대표 밑으로 붙암 즉, 두 팀을 하나의 팀으로 합친다.
n, m = map(int, input().split()) # 정점 개수 n, 간선 개수 m 입력

# 3. 부모 테이블 초기화
# 처음에는 모든 노드가 자기 자신이 대표
# 예: n=5면 parent = [0, 1, 2, 3, 4, 5]
parent = [i for i in range(n + 1)]

# 4. 모든 간선을 보면서 연결된 노드끼리 같은 팀으로 합치기
for _ in range(m):
    u, v = map(int, input().split())
    union(parent, u, v)

# 5. 연결 요소 개수 세기
# (자기가 자기 자신의 대장인 경우만 카운트)
count = 0
for i in range(1, n + 1):
    if parent[i] == i: # 즉, parent[i] == i 인 노드 개수를 센다.
        count += 1

print(count)