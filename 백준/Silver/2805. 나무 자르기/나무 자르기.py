# https://www.acmicpc.net/problem/2805
# 2805 나무 자르기
# 알고리즘: 이분탐색
# 핵심: 완성하면 멈춘다 X -> 모든 경우의 수를 계산, mid 최댓값 출력

'''
나무 길이가 m보다 길때만 (나무길이 - m)만큼의 나무를 얻을 수 있음

1. 모든 나무들의 합 나누기 개수 /  평균을 구하고
settings: 평균 - (m / 나무 개수) 
초기값일때 계산한 값 = cut_timber
--> 모든 나무의 차이가 클 경우에 비효율적임

2. 절단기 높이를 작으면 내리고 크면 올리기
설정값을 줄여야함 -> 하나씩 -> 이분 탐색

3. 이분 탐색
종료조건을 생각하는게 힘들었음 -> 종료한다는 생각 X!
'''

import sys
input = sys.stdin.readline

#n: 나무의 수 m: 목표 나무 길이
n, m = map(int, input().split())
trees = list(map(int, input().split()))

def cal_cut(mid)->int:
    # 자른 나무 계산
    global trees
    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid
    return total

def binary_search(target, start, end):
    global cutter_height
    if start>end:
        return None
    mid = (start+end)//2
    cal = cal_cut(mid)
    if cal < target:
        binary_search(target, start, mid-1)
    if cal >= target:
        cutter_height = mid
        binary_search(target, mid+1, end)


low = 0
high = max(trees)
cutter_height = 0

binary_search(m, low, high)
print(cutter_height)
