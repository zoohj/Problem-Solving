#1158 요세푸스 문제
'''
N명의 사람, K번째 사람을 제ㄱ
원에서 사람들이 제거되는 순서
'''

import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
q=deque(range(1,n+1))
result = []

while q:

    # k명만큼 앞에서 뒤로 보냄
    q.rotate(-k)
    result.append(str(q.pop()))
    # print(result)


print("<" + ", ".join(result) + ">")