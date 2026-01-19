#11399 ATM
'''
가장 적게 걸리는 사람부터 하고 합을 구하자
'''

import sys
input = sys.stdin.readline

n = int(input())
times=list(map(int, input().split()))

times.sort()

sum_time = [0]*n
sum_time[0] = times[0]
for i in range(1,n):
    sum_time[i] = times[i] + sum_time[i-1]
print(sum(sum_time))