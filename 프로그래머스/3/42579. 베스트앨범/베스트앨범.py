from collections import defaultdict
import heapq
def solution(genres, plays):
    answer = []
    music_total = defaultdict(int)
    music_sort = {}
    
    for i in range(len(genres)):
        music_total[genres[i]] += plays[i]
        if genres[i] not in music_sort:
            music_sort[genres[i]] = []
         
        heapq.heappush(music_sort[genres[i]],(plays[i], i))
    
    
    music_total = sorted(music_total.items(), key = lambda x:x[1], reverse = True)
   
    for key,value in music_total:
        musics = heapq.nlargest(2,music_sort[key], key= lambda x: (x[0],-x[1]))
        for music in musics:
            answer.append(music[1])
    
    return answer