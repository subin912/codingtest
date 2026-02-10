def solution(genres, plays):
    answer = []
    genre_dict = {} #장르 저장
    total = {} #장르별 총 재생수 저장
    
    for i in range(len(genres)): # i=노래고유번호
        g = genres[i] #장르 ["classic", "pop", "classic"]
        p = plays[i] #노래 재생 반복수  [500, 600, 150]

        # 이제 dict로 저장하기 위한 단계
        if g not in genre_dict: #처음보는 애면 넣어주자
            genre_dict[g] = []
            total[g] = 0   #처음은 0

        genre_dict[g].append((p, i)) 
        #{'classic': [(500, 0), (150, 2)], 'pop': [(600, 1)]}
        total[g] = total[g] + p    #이 장르 총 재생수 더하기
        #total["classic"] = total["classic"] + 500 => total = {"classic": 500}

    #장르를 총재생수 기준으로 내림차순 정렬하기     
    sorted_genres = sorted(total.items(), key=lambda x: x[1], reverse=True) #x[1] = 총재생수 650, 600, 120 등등
    #[("classic", 650), ("pop", 600), ("jazz", 120)] 이런식으로 나옴. items() 하면 키,값 둘다 나온다!
    
    for g, c in sorted_genres: #g= 장르 name ,c = 그 장르의 총 재생수
        songs = genre_dict[g] #장르의 노래들 꺼내기 #songs = [ (500,0), (150,2), (800,3) ]
        
        # 재생수 내림차순, 재생수 같으면 고유번호 오름차순 (재생수 큰 노래부터, 재생수 같으면 번호 작은노래부터)
        songs.sort(key=lambda x: (-x[0], x[1])) 

        # 앞에서 최대 2개만 추가
        answer.append(songs[0][1]) #재생수 제일큰 노래의 번호 ex) (2500,4) ->> 4
        if len(songs) > 1: #2개 이상이면 2등도 추가.
            answer.append(songs[1][1])

    return answer

#즉, 인기장르별 차례로 가서, 그 장르에 인기 노래 2개씩만 뽑음.
