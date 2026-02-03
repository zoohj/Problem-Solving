# https://www.acmicpc.net/problem/1966
# 1966 프린터 큐
# 알고리즘: deque
# 핵심: 차분히 구현하자

"""
FIFO que
중요도 확인
현재문서보다 중요도가 높은 문서가 있으면 q뒤로 보내

우선순위 몇개인지 저장해놓고 그 수만큼 반복
우선순위(1~9)

"""

import sys

input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
    n, curious = map(int, input().split())
    importance = list(map(int, input().split()))

    # 중요도 개수 저장 배열 선언 (0은 비워두고 1~9)
    importance_count = [0] * 10
    for imp in importance:
        importance_count[imp] += 1

    # deque에 (문서번호, 중요도) 튜플로 저장
    # deque([(0, 1), (1, 1), (2, 9), (3, 1), (4, 1), (5, 1)])
    dq = deque((i, v) for i, v in enumerate(importance))
    count = 0

    # 중요도 높은 순부터 역순으로 탐색
    for i in range(9, 0, -1):
        for _ in range(importance_count[i]):
            # 원하는 중요도가 아닌 경우 뒤로 보냄
            while dq[0][1] != i:
                dq.rotate(-1)

            count += 1
            idx, _ = dq.popleft()
            # 궁금한 문서가 인쇄된 경우 count 저장
            if idx == curious:
                print(count)
                break  # 안쪽 for문 탈출
        # for가 break없이 끝났을 때(궁금한 문서 순서 찾았을 경우)
        else:
            continue  # 안쪽 for문이 정상종료 되면 실행 (아직 못찾고 다음 중요도 넘어가)
        break  # 바깥 for문 탈출 (전체 종료)
