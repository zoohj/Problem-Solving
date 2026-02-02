# https://www.acmicpc.net/problem/1654
# 1654 랜선 자르기
# 알고리즘: 이분탐색
# 핵심: 재귀 범위 설정 유의


def binary_search(start,end,target): #target은 필요한 랜선 개수
    global max_len
    if start > end:
        return None
    mid = (start+end)//2
    if mid == 0: # 0으로 나누기 방지
        binary_search(mid + 1, end, target)
        return None
    
    cable_count=cut_cable(mid)
    if cable_count < target:
        binary_search(start, mid-1, target)
    if cable_count >= target:
        if mid >= max_len:
            max_len = mid
        binary_search(mid+1, end, target)


# 개수 파악
def cut_cable(a):
    count = 0
    # a는 자를 길이, 개수가 맞는지 확인해야할듯?
    for cable in cables:
        count += cable//a
    return count

 
import sys
input = sys.stdin.readline

k, n  = map(int, input().split())

cables=[]
for _ in range(k):
    cables.append(int(input()))

cables_total = sum(cables)
avg=cables_total//n

max_len = 0

low = 1
high = avg

binary_search(low,high,n)
print(max_len)
