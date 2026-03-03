# https://www.acmicpc.net/problem/1238
# 1238 파티
# 알고리즘: 다익스트라
# 핵심:

from collections import deque
import heapq
import sys

input = sys.stdin.readline

"""
n개의 숫자로 구분된 각각의 마을 한명의 학생
n명의 학생이 x마을로 가야함
m개의 단방향 도로
i번째 길을 지나가는데 시간 소비(가중치가 다름)
가장 많은 시간 소비하는 학생

다시 그들의 마을로 돌아와야함! (왕복을 계산해야함)
"""

# 시작점, 끝점, 가중치

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    # 간선 입력
    graph[s].append((e, w))  # 내가 어디로 갈 수 있는지 적어둔 표


def dijkstra(start, end):
    # 시작점에서 각 노드까지 현재까지 알고 있는 최소 시간
    distance = [float("inf")] * (n + 1)  # 무한대로 초기화시켜놓음
    distance[start] = 0
    # q는 걍 그건가보다 stack?
    heap = []
    # 가장 작은 값부터 꺼내주는 상자, 지금까지 발견한 노드중에 가장 가까운애를 꺼내주도록 도와줌
    heapq.heappush(heap, (0, start))  # (거리, 노드번호) distance[start],start 넣은건가?
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
    return distance[end]


max_t = []

# 1에서 x, 2에서 x, 3에서 x,
for i in range(1, n + 1):
    min_time_person = dijkstra(i, x) + dijkstra(x, i)
    heapq.heappush(max_t, -min_time_person)

print(-heapq.heappop(max_t))
