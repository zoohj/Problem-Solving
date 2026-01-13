#2563 색종이
'''
가로세로 크기 100
10인 정사각형 검은 종이 n개
검은 영역의 넓이 구하기

1. 2차원 리스트를 다 0으로 채워 -> 색칠 X
2. 반복문으로 돌면서 도화지 값을 1로 바꾸고
3. 전체 도화지에서 1의 개수를 출력
'''

import sys
input = sys.stdin.readline

papaer_count = int(input().rstrip())
paper = [[0]*100 for _ in range(100)]

for _ in range(papaer_count):
    n,m = map(int, input().split())    
    for i in range(n, n+10):
        for j in range(m, m+10):
            paper[i][j] = 1     # 도화지 색칠

total = sum(row.count(1) for row in paper)
print(total)
