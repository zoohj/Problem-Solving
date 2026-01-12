#2161 카드1
'''
N장의 카드 순서대로
버린 카드 순서대로 출력
'''

import re
import sys
input = sys.stdin.readline

n = int(input()) 

from collections import deque
q = deque(range(1,n+1))

for _ in range(n-1):
    #삭제
    poped_el = q.popleft()
    print(poped_el)
    # 뒤로 이동
    poped_el = q.popleft()
    q.append(poped_el)
print(q.pop())