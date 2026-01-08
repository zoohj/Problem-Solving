#9012 괄호
'''
() 괄호가 잘 닫혀있으면 VPS
output: VPS 여부 (YES/NO)
'''

import sys
input = sys.stdin.readline

t = int(input()) # 반복횟수

# 왼쪽에서 이동하고 괄호를 숫자로 생각해서 생각해보자
# "("" = 1, ")" = -1 => 최종이 0이 되어야하고, 왼쪽에서 오른쪽으로 진행하는 도중에 음수가 되면 안됨

for _ in range(t):
    ps = str(input().strip())

    total = 0
    check = 1
    for i in range(len(ps)):
        if ps[i]=='(':
            total += 1
        elif ps[i]==')':
            total -= 1
        
        if total < 0:
            check=0
            break 
    else:
        if total == 0:
            pass
        elif total > 0:
            check=0

    if check:
        print("YES")
    else:
        print("NO")