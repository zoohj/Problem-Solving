# https://www.acmicpc.net/problem/1717
# 1717 집합의 표현
# 알고리즘: union-find


import sys

input = sys.stdin.readline


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        # ⭐️⭐️⭐️
        parent[root_y] = root_x


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]


for _ in range(m):
    z, a, b = map(int, input().split())
    # 0일때 union하고 1일때 확인
    if z == 0:
        union(a, b)
    else:
        print("YES" if find(a) == find(b) else "NO")

