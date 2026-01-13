#10845 큐
'''
큐 구현 (Deque 사용)
'''



from collections import deque
import sys
input = sys.stdin.readline

class Que(deque):
    def __init__(self):
        super().__init__()

    def push(self, num):
        self.append(num)
    def item_pop(self):
        if not self:
            print("-1")
        else:
            print(self.popleft())

    def size(self):
        return print(len(self))
    def empty(self):
        if not self:
            return print(1)
        return print(0)

    def front(self):
        if self:
            return print(self[0])
        else: 
            print("-1")
    def back(self):
        if self:
            return print(self[-1])
        else: 
            print("-1")

n = int(input())
qu = Que()

commands= {
    "pop": qu.item_pop,
    "size": qu.size,
    "empty": qu.empty,
    "front": qu.front,
    "back": qu.back
}

for _ in range(n):
    line = input().split()
    command = line[0]

    if command == "push":
        num = line[1] 
        qu.push(num)
    
    elif command in commands:
        commands[command]()   #딕셔너리에서 함수 꺼내서 바로 호출
