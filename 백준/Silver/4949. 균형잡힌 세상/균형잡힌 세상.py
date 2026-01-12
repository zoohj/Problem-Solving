#4949 균형잡힌 세상
'''
"()", "[]"
방법 1. deque
방법 2. stack

중 deque로 구현
'''

import sys
input = sys.stdin.readline
from collections import deque

# deque로 구현
while True:

    test_case = str(input().rstrip())
    if test_case == ".":
        break
    q = deque()
    wrong = 0
    
    for str_t in test_case:
        if str_t == "(" or str_t == "[":
            q.append(str_t)
        if str_t == ")":
            if q and q[-1]== "(":
                q.pop()
            else:
                wrong = 1
        if str_t == "]":
            if q and q[-1]== "[":
                q.pop()
            else:
                wrong = 1

    if wrong == 0 and not q:
        print("yes")
    else:
        print("no")
