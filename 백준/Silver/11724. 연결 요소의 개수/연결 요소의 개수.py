# https://www.acmicpc.net/problem/11724
# 11724 연결 요소의 개수
# 알고리즘: dfs
# 핵심: 이중리스트 구현, visited 배열, 재귀

"""
방향없는 그래프
정점 개수 N
간선 개수 M
간선의 양 끝점 u, v
"""

import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def dfs(start):
    # x 방문처리
    # x와 연결된 모든 정점 중, 아직 방문 안한 정점으로 재귀/반복 이동
    """
    기준은 정점 start
    i가 방문 안됐으면 새 연결요소 발견
    i에서 DFS 시작 -> 연결된 모든 정점을 visited = 1로 처리
    """
    visited[start] = 1
    for tree in trees[start]:
        if visited[tree] == 0:
            visited[tree] = 1
            dfs(tree)
        else:
            pass


n, m = map(int, input().split())
trees = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
count = 0

for i in range(m):
    a, b = map(int, input().split())
    trees[a].append(b)
    trees[b].append(a)


for i in range(1, n + 1):
    if visited[i] == 0:
        dfs(i)
        count += 1

print(count)
