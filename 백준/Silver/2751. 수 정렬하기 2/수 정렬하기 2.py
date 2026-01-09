#2751 수 정렬하기 2
'''
input: 정수 개수 n, nums(수의 중복 x)
output: 오름차순 정렬
'''

import sys
input = sys.stdin.readline
n = int(input()) # 개수

num_list =[]
for i in range(n):
    num = int(input().strip())
    num_list.append(num)
num_list.sort()

for i in num_list:
    print(i)