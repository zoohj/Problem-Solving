# 1. que에 시작좌표(0,0) 넣기
# 2. que에서 좌표 하나 꺼내 상하좌우 살핌(dx,dy)
# 3. ⭐️ 범위 안, 값이 1인 곳을 찾으면 한칸 이동
# 4. 그 좌표를 다시 큐에 넣음(살펴봐야하는 좌표 저장)
# 5. 큐가 빌때 까지 반복 

# 목적지의좌표(n,m)에 들어있는 값이 최소값

from collections import deque

def solution(maps):
    n=len(maps)
    m=len(maps[0])
    
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]    
    
    queue = deque([(0,0)])
    
    while queue:
        x,y=queue.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny=y+dy[i]
            # 배열 인덱스 에러 방지
            if 0 <= nx < n and 0 <= ny < m:
                # 1을 넘는다면 이미 더 빠른 길로 누군가가 왔다는 의미이므로, 지나감
                if maps[nx][ny]==1:
                    maps[nx][ny] =maps[x][y] +1 # 한칸 이동
                    queue.append((nx,ny))
                    
    answer = maps[n-1][m-1]
    
    return answer if answer  > 1 else -1
