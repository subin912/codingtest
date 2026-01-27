from collections import deque

def solution(people, limit):
    answer = 0
    people.sort() #정렬하기
    people = deque(people)
    #print (people) 
    
    while len(people) > 0:
        if len(people) == 1:
            people.pop()
            answer = answer + 1 
        else:
            if people[0] + people[-1] > limit:
                people.pop()
                answer = answer + 1
            else:
                people.popleft()
                #people.pop(0)
                people.pop()
                answer = answer + 1

    return answer