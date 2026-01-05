#10807 개수 세기[배열]
'''
input: 정수의 개수 N, 정수 입력, 정수 v
ouput: 정수 v가 몇개?
'''

import sys
N= int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
v= int(sys.stdin.readline())
count=0

for i in lst:
    if i == v:
        count +=1

print(count)

