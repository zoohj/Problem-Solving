# sort로 정렬해야하나? => heapq로 효율적으로 구현

# heapq: 우선순위 큐(Priority Queue)
# 데이터 추가, 제거할때마다 순서 재배치(오름,내림)

# 최소가 K를 넘을때까지
# 안넘으면 -1 return하면 되고
# 섞어서(최소 스코빌 하나 + 두번째 작은 스코빌 *2) 다시 넣기

import heapq
    

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    # 가장 작은 스코빌 지수가 k보다 작을 동안 반복
    while scoville[0] < K:
        # 불가능한 경우 -1 반환
        if len(scoville)<2:
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        mixed = first+(second*2)
        # 섞어서 다시 넣기
        heapq.heappush(scoville,mixed)
        
        answer +=1
    return answer