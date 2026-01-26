# https://www.acmicpc.net/problem/1003
# 1003 피보나치 함수
# 알고리즘: dp
# 핵심: 재귀로 구현하니까 시간초과남


import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a, b = 1,0
    for _ in range(n):
        a, b = b, a+b
    print(a,b)

