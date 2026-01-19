from collections import deque

def solution(priorities, location):
    queue = deque() # 이제 여기에 (인덱스,우선순위)으로 들어가야함, 인덱스는 첨위치 기억용.
    for i in range(len(priorities)):
        queue.append((i, priorities[i]))
		# 예: priorities = [2,1,3,2]
        # queue = [(0,2), (1,1), (2,3), (3,2)]
    ## 일단 위 과정은 인덱스, 우선순위 튜플 만들어주기 완료.    
    answer = 0
		# 이제 시작
    while True: # 내가 찾는 프로세스 실행되면 return으로 종료
        idx, p = queue.popleft() #차례로 입장시키기
					
        if queue and p < max(q[1] for q in queue): #queue가 비어있으면 max 실행안됨
            queue.append((idx, p)) #que가 비어있지x, 뒤에 나보다 순위 높은 애 있으면 뒤로가 
        else: #뒤에 우선순위 높은거 없으면 더해라.
            answer = answer + 1 

            if idx == location: #우리가 찾던 첨 위치 프로세스라면 그만.
                return answer


## 다른 풀이?
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
