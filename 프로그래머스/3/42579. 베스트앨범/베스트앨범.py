def solution(genres, plays):
    answer = []
    
    diction = {}
    for genre, cnt in zip(genres, plays):
        diction[genre] = diction.get(genre, 0) + cnt
    
    sorted_genres = sorted(diction, key=lambda x: diction[x], reverse=True)
    
    for genre in sorted_genres:
        songs = []
        for idx, (g, p) in enumerate(zip(genres, plays)):
            if g == genre:
                songs.append((idx, p))
        
        songs.sort(key=lambda x: (-x[1], x[0]))
        
        for i in songs[:2]:
            answer.append(i[0])
    
    return answer