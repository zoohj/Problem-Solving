#10871 X보다 작은 수
'''
input: 정수 N개로 이루어진 수열 A, 정수 X
ouput: A에서 X보다 작은 수 출력
'''

import sys

N,X= map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
# print(A)

for a in A:
    if a < X:
        print(a, end=" ")

print()