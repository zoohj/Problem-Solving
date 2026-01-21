#2606 바이러스
'''
1번 컴퓨터와 연결되어있는 모든 컴퓨터
'''

from collections import deque
import sys
input = sys.stdin.readline

n = int(input()) # 컴퓨터 수
v = int(input()) # 연결된 컴퓨터쌍

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
count=0

for _ in range(v):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# 재귀함수
def dfs(now):
    global count
    visited[now]= True
    for next_node in graph[now]:
        if not visited[next_node]:  # 방문을 안한 경우
            count +=1
            dfs(next_node)

dfs(1)
print(count)