# https://www.acmicpc.net/problem/18352
# 18352 특정 거리의 도시 찾기
# 알고리즘: BFS
# 핵심: 가중치 1일때, 최단거리 계산은 BFS

from collections import deque
import sys

input = sys.stdin.readline

"""
최단거리가 k인 도시 찾기
존재하지않으면 -1
최단거리들 계산하고 k인거 출력
모든 도시를 오름차순, 없으면 -1
최단거리 어떻게 구하지 => distance 배열 만들기
방향이 있는 노드니까 그냥 하나만 연결하면 됨
도시개수 n(노드 개수), 도로 개수 m(vertax num), K(원하는 거리), X(출발도시)
"""

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    # 간선 입력
    graph[a].append(b)

# 방문 여부 + 거리 저장을 같이 처리
# distance[i]==-1 아직 방문 안한 노드
# distance[next]=distance[cur]+1
distance = [-1] * (n + 1)
distance[x] = 0

queue = deque()

# queue에 시작점(x) 먼저 넣기
queue.append(x)

while queue:
    # 큐에서 하나 꺼냄 → cur
    cur = queue.popleft()
    # cur에서 갈 수 있는 모든 next 확인
    for next in graph[cur]:
        # distance[next] == -1 이면
        # → distance[next] = distance[cur] + 1
        # → 큐에 추가
        if distance[next] == -1:
            distance[next] = distance[cur] + 1
            queue.append(next)

# 방문 여부 체크
found = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        found = True

if not found:
    print(-1)
