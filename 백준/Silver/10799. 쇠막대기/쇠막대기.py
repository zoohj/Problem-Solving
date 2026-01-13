#10799 쇠막대기
'''
괄호 () -> 레이저
어떻게 수학적으로 자를수있을까
우선 괄호문제니까 deque에 넣어보자
그리고 만약에 닫힌 괄호를 넣었을 때 바로 열린 괄호가 되면...레이저야 -> 왼쪽에 있던 괄호들이 다 잘라지는거야

왼쪽에 몇개가 있는지 기억하고있어야하겠네 left_side_count = 0
왼쪽에 3개가 있었는데 레이저가 나오면 +i개
닫힌 괄호가 나오면 count +1 하고 left_side_count-1
열린 괄호 나오면 count +1해, left_side_count+1
'''

from collections import deque
import sys
input = sys.stdin.readline

sticks = input().strip()
q = deque()
count =0
left_side_count=0

# 왼쪽 괄호 나오면 q에 넣고 하고 a +1
# 오른쪽 괄호가 나왔는데 왼쪽이 열린괄호 아니면 count + 1 하고 a-1
    # 오른쪽 괄호 나왔는데 그 전에 왼쪽 괄호가 바로 있었으면 레이저야 => 왼쪽에 있던 막대(a) 잘라 count+=left_side

for stick in sticks:
    if stick == "(":
        q.append(stick)
        left_side_count+=1      # 우선 막대가 시작한다고 가정
    elif stick == ")":
        if q[-1] == "(":        # 막대가 아닌 레이저인 경우, 레이저로 잘라졌을 때 조각 추가
            left_side_count -=1
            count += left_side_count
        else:                   # 막대기의 끝이 나올 때, 조각 추가
            count+=1
            left_side_count-=1
        q.append(stick)
print(count)