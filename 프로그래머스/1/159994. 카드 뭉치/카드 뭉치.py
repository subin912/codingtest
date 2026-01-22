def solution(cards1, cards2, goal):
    for i in goal:
        # cards1의 맨 앞과 같다
        if cards1 and cards1[0] == i:
            cards1.pop(0)
        # cards2의 맨 앞과 같다    
        elif cards2 and cards2[0] == i:
            cards2.pop(0)
        else:
            return 'No'
    return 'Yes'