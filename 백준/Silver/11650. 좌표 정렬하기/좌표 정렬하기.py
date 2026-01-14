#11650 좌표 정렬하기
'''
2차원 평면 위에 점 N개
x좌표를 증가하는 순 (오름차순)
x좌표가 같으면 y좌표 증가하는 순서
'''


import sys
input = sys.stdin.readline

n = int(input())

dot = []
for _ in range(n):
    a, b = map(int, input().split())
    dot.append((a,b))

dot.sort()

for point in dot:
    print(*point, end=" ")
    print()