#13335 트럭
'''
n개의 트럭
다리길이 - w대의 트럭만 가능
다리 최대하중 L

최대 w대의 트럭이 다리에 올라갈 수 있음
if 다리위에 있는 트럭의 무게 합이 L을 넘는 경우 -> 트럭 리스트 pop 하지 않음
모든 트럭이 다 이동할 때까지 => deque가 다 비워질때까지
'''

import sys
input = sys.stdin.readline
from collections import deque

n, w, l = map(int, input().split())

truck_w = deque(map(int, input().split())) # 트럭

#다리
bridge = deque()
for _ in range(w):
    bridge.append(0)

count = 0 # 횟수

truck_on_bridge_weight=0

# 전진 로직: bridge.popleft() -> brideg.append(원소 or 0)

while bridge:
    ## ========= point!! ========= ##
    count +=1
    out = bridge.popleft()
    truck_on_bridge_weight -= out
    ## =========================== ##

    if truck_w:
        if truck_on_bridge_weight +truck_w[0] <= l:
            truck = truck_w.popleft()
            bridge.append(truck)
            truck_on_bridge_weight += truck
        else:
            bridge.append(0)

print(count)