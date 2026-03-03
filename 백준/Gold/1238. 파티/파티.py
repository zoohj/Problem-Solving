# https://www.acmicpc.net/problem/1238
# 1238 파티
# 알고리즘: 다익스트라
# 핵심: 역방향 그래프의 이해

from collections import deque
import heapq
import sys

input = sys.stdin.readline

def dijkstra(start, graph):
    # 시작점에서 각 노드까지 현재까지 알고 있는 최소 시간
    distance = [float("inf")] * (n + 1)  # 무한대로 초기화시켜놓음
    distance[start] = 0
    # heap 리스트 선언, heapq에 인자로 넘겨줌
    heap = []
    # 가장 작은 값부터 꺼내주는 상자, 지금까지 발견한 노드중에 가장 가까운애를 꺼내주도록 도와줌
    heapq.heappush(heap, (0, start))  # (거리, 노드번호)
    while heap:
        # 지금까지 발견된 것 중 가장 가까운 노드
        dist, now = heapq.heappop(heap)  #

        if distance[now] < dist:  # now번 노드로 가는 길이가 가중치(dist)보다 작은 경우?
            continue  # 아래 로직 Pass

        # 시작점 -> now -> next로 가는 거리 계산
        for next, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next]:
                distance[next] = new_cost
                heapq.heappush(heap, (new_cost, next))  # (거리, 노드번호)
    return distance


# 시작점, 끝점, 가중치

n, m, x = map(int, input().split())
# 정방향 그래프 (X → i 계산용)
graph = [[] for _ in range(n + 1)]
# 역방향 그래프 (i → X 계산용)
reverse_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    # 간선 입력
    graph[s].append((e, w))  # 내가 어디로 갈 수 있는지 적어둔 표
    reverse_graph[e].append(
        (s, w)
    )  # 어짜피 반대로 가도 길은 계산은 똑같으니까 퍼트리려고 임의로 뒤집음

# X → 모든 마을 거리
dist_from_x = dijkstra(x, graph)
# 모든 마을 → X 거리
dist_to_x = dijkstra(x, reverse_graph)

answer = 0
for i in range(1, n + 1):
    # 왕복 시간 중 최대값 찾기
    answer = max(answer, dist_from_x[i] + dist_to_x[i])

print(answer)

