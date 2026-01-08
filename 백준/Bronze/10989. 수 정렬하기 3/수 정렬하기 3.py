#10989 수 정렬하기 3
'''
input: N개의 수
ouput: 오름차순 정렬 결과
'''

import sys
input = sys.stdin.readline


count = [0] * 100001

n= int(input())

num_list = []
for _ in range(n):
    num = int(input())
    count[num] += 1

for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)