#1764 듣보잡
'''
듣도 못한 사람
보도 못한 사람
듣도보도못한사람명단
교집합, 사전순 sort
'''

import sys
input = sys.stdin.readline

n, m = map(int,input().split())

unheard = set()
for _ in range(n):
    unheard.add(input().rstrip())
unseen = set()
for _ in range(m):
    unseen.add(input().rstrip())
intersection = unheard&unseen
sort_intersection=sorted(intersection)
print(len(sort_intersection))
for answer in sort_intersection:
    print(answer)