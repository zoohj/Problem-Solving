#10845 큐
'''
큐 구현 (Circualr Queue 원형 큐 사용!)
'''

import sys
input = sys.stdin.readline

class Que:
    def __init__(self):
        self.max_size = n +1
        self.data = [0] * self.max_size
        self.front_idx = 0 
        self.rear_idx = 0

    def push(self, num):
        self.rear_idx = (self.rear_idx +1) % self.max_size
        self.data[self.rear_idx]=num
        
    def item_pop(self):
        if not self.front_idx == self.rear_idx:
            self.front_idx =(self.front_idx+1)%self.max_size
            answer = self.data[self.front_idx]
            return answer
        return -1

    def size(self):
        # 해라
        size = (self.rear_idx - self.front_idx + self.max_size) % self.max_size
        return size
    
    def empty(self):
        if self.front_idx == self.rear_idx:
            return 1
        return 0

    def front(self):
        if self.front_idx==self.rear_idx:
            return -1
        location = (self.front_idx + 1)% self.max_size
        answer = self.data[location]
        return answer

    def back(self):
        if self.front_idx==self.rear_idx:
            return -1
        answer = self.data[self.rear_idx]
        return answer


n = int(input())

MAX_SIZE = 10000

que = Que()

commands= {
    "pop": que.item_pop,
    "size": que.size,
    "empty": que.empty,
    "front": que.front,
    "back": que.back
}

for _ in range(n):
    line = input().split()
    command = line[0]

    if command == "push":
        num = line[1] 
        que.push(num)
    
    elif command in commands:
        print(commands[command]())  
