#10773 제로
'''
재현 - 잘못된 수를 부를 때마다 0 -> 그 전에  쓴 수 지워
모든 수를 받아 적은 후 그 수의 합
'''

from collections import deque
import sys
input = sys.stdin.readline

k = int(input())
q = deque()

for  _ in range(k):
    k = input().rstrip()
    if k == '0':
        if q:
            q.pop()
    else:
        q.append(int(k))

print(sum(q))