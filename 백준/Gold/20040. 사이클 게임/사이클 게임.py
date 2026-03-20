# https://www.acmicpc.net/problem/20040
# 20040 사이클 게임
# 알고리즘: union-find


import sys

input = sys.stdin.readline


def find(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a


def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        parent[root_b] = root_a


n, m = map(int, input().split())

parent = [i for i in range(n)]

for i in range(1, m + 1):
    x, y = map(int, input().split())
    if find(x) == find(y):
        print(i)
        break
    else:
        union(x, y)

else:
    print(0)