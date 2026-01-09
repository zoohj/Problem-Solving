#10828 스택
'''
정수 저장 스택 구현
1. push X : 정수 x를 스택에 넣음
2. pop : 가장 위에있는 정수 빼고 출력, 비어있으면 -1
3. size : 스택에 들어있는 정수의 개수
4. empty : 스택이 비어있는지 확인 (1(비어있음),0)
5. top : 가장 위에있는 정수 출력, 비어있으면 -1
'''

class Node:
    def __init__(self,data):
        self.data = data # data
        self.next = None # 다음 주소

class Stack:
    def __init__(self):
        self.top = None # ⭐️
        self.count = 0

    def push(self, data):
        if not self.top:
            self.top = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.top
            self.top = new_node
        self.count += 1

    def pop(self):
        if not self.top:
            return -1
        result = self.top.data
        self.top = self.top.next
        self.count -= 1
        return result

    def size(self):
        # ⭐️⭐️⭐️
        return self.count

    def empty(self):
        if not self.top:
            return 1
        return 0

    def peek(self):
        if not self.top:
            return -1
        node = self.top
        return node.data


import re
import sys
input = sys.stdin.readline
n = int(input()) # 명령의 수

stack= Stack()

for _ in range(n):
    word= input().strip() 
    
    command = word.split()
    if command[0] == "push": # command[0]: "push" / command[1]: {n}
        num = int(command[1])
        stack.push(num)
    elif command[0] == "pop":
        print(stack.pop())
    elif command[0] == "size":
        print(stack.size())
    elif command[0] == "empty":
        print(stack.empty())     
    elif command[0] == "top":
        print(stack.peek())