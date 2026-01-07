#2775 부녀회장이 될테야
'''
아파트 거주 조건
a층 b호 거주: (a-1)층 1~b호 사람들 수의 합만큼 데려와서 살아야함

input: k층, n호
output: k층, n호에 거주하는 인원 수
'''

import sys
input = sys.stdin.readline

t_count = int(input())

for _ in range(t_count):
    k = int(input())
    n = int(input())
    # 2차원 배열 할당
    apt = []
    for i in range(k+1):
        floor = []
        for j in range(n+1):
            floor.append(0)
        apt.append(floor)

    # 0층 초기화
    for j in range(1, n+1):
        apt[0][j]=j
    
    # 1~k층, 1~n호
    for i in range(1, k+1):
        for j in range(1,n+1):            
            apt[i][j] = apt[i-1][j]+apt[i][j-1]
    
    print(apt[k][n])