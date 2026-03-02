def solution(genres, plays):
    songs = []
    ## (1) 데이터 수집
    # 1. zip으로 장르와 재생수를 묶고
    # 2. enumerate로 번호(i)를 붙이기.
    for i, (g, p) in enumerate(zip(genres,plays)):
        songs.append((i,g,p)) #3. append 사용해 리스트에 하나씩 추가
    
    ## (2) 장르별 그룹화 및 합계 계산
    genre_total = {} #4. 장르별 총 재생 횟수 (누가 1등 장르인지 알기 위해)
    genre_songs = {} # 5. 장르별 곡 목록 (장르 내에서 누가 1등 곡인지 알기 위해)
    
    for i, g, p in songs:
        # 처음 보는 장르라면 0으로 초기화
        if g not in genre_total:
            genre_total[g] = 0
            genre_songs[g] = []
        
        genre_total[g] += p # 합계 더하기
        genre_songs[g].append((p, i)) # (재생수, 고유번호)를 장르별 리스트에 추가
    
    # (3) 인기 장르 순으로 정렬 -> 장르 이름들을 가져와, '장르별 합계' 기준 내림차순 정렬
    sorted_genres = sorted(genre_total.keys(), key=lambda x: genre_total[x], reverse=True)
    # (4) 각 장르 내에서 베스트 2곡 선정
    answer = []
    for g in sorted_genres:
        # 재생수 높은 순 -> 번호 낮은 순
        genre_songs[g].sort(key=lambda x: (-x[0], x[1])) # # (재생수가 같으면 ID가 작은 순서대로 정렬되도록 설정)
        for p, i in genre_songs[g][:2]: # 상위 2개만 정답 리스트에 추가 (슬라이싱 [:2] 사용)
            answer.append(i)
            
    return answer


# ##################
# def solution(genres, plays):
#     answer = []
#     genre_dict = {} #장르 저장
#     total = {} #장르별 총 재생수 저장
    
#     for i in range(len(genres)): # i=노래고유번호
#         g = genres[i]
#         p = plays[i]

#         # 이제 dict로 저장하기 위한 단계
#         if g not in genre_dict: #처음보는 애면 넣어주자
#             genre_dict[g] = []
#             total[g] = 0   #처음은 0

#         genre_dict[g].append((p, i))
#         total[g] = total[g] + p    #장르 총 재생수 더하기

#     #장르를 총재생수 기준으로 내림차순 정렬하기     
#     sorted_genres = sorted(total.items(), key=lambda x: x[1], reverse=True) 
    
#     for g, c in sorted_genres: #g= 장르name ,c = 그 장르의 총 재생수
#         songs = genre_dict[g] #장르의 노래들 꺼내기
        
#         # 재생수 내림차순, 재생수 같으면 고유번호 오름차순
#         songs.sort(key=lambda x: (-x[0], x[1])) 

#         # 앞에서 최대 2개만 추가
#         answer.append(songs[0][1]) #재생수 제일큰 노래의 번호 ex) (2500,4) ->> 4
#         if len(songs) > 1: #2개 이상이면 2등도 추가.
#             answer.append(songs[1][1])

#     return answer

# #즉, 인기장르별 차례로 가서, 그 장르에 인기 노래 2개씩만 뽑음.
