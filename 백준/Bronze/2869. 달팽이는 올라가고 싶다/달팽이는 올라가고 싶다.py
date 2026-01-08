#2869 달팽이는 올라가고 싶다
'''
나무막대 높이 V
달팽이(낮:A미터, 밤:-B미터)
input: A미터, B미터, V미터
output: 정상까지 올라가는데 걸린 날짜
'''

import sys
input = sys.stdin.readline

a,b,v= map(int,input().split())

#hint 마지막날에 올라갈 A를 빼고 생각해!!

day = (v-a)//(a-b)

if (v-a)%(a-b) == 0:
    # 마지막날 올라갈 하루 더하기
    day += 1
else:
    # 마지막날 빼고 하루를 더 써야함    
    day += 2

print(day)