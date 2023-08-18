def solution(cacheSize, cities):
    # 예외처리
    if cacheSize == 0:
        answer = 5 * len(cities)
        return answer
    else:
        cnt = 1 # 우선순위
        pages = [] # 페이지 리스트
        pages.append([cities[0],cnt])
        answer = 5
        for i in range(1,len(cities)):
            pages.sort(key=lambda x:x[1])
            # 도시가 페이지 안에 없고 아직 공간이 남아있다면 넣어주기
            if cities[i].lower() not in[page[0] for page in pages] and len(pages) < cacheSize:
                # 우선순위 바꿔직
                cnt += 1
                pages.append([cities[i].lower(),cnt])
                # 실행시간 더해주기
                answer += 5
                continue
            # 도시가 페이지 안에 있을 때
            elif cities[i].lower() in [page[0] for page in pages]:
                for page in pages:
                    if cities[i].lower() == page[0]:
                        # 우선순위만 바꿔주기
                        cnt += 1
                        page[1] = cnt
                        # 실행시간 더해주기
                        answer += 1
                        exit()
            # 도시가 페이지 안에 없고 공간도 없을 때
            if cities[i].lower() not in pages and len(pages) == cacheSize:
                # 페이지 바꿔주기
                pages[0][0] = cities[i].lower()
                # 우선순위 바꿔주기
                cnt += 1
                pages[0][1] = cnt
                #실행시간 더해주기
                answer += 5
                continue
        print(answer)
        return answer
solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])