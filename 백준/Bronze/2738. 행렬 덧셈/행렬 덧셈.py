#2738 행렬 덧셈[배열]
'''
input: 행열 크기 N,M(N*M), 행렬 A, B의 원소들
ouput: 행렬 A,B 덧셈결과
'''

import sys
n, m= map(int, sys.stdin.readline().split())
matrix1 = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
matrix2 = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

result= [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        result[i][j]=matrix1[i][j]+matrix2[i][j]

for row in result:
    for val in row:
        print(val, end=" ")
    print()
