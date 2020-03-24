# 18258번 queue2
# input()보다 sys.stdin.readline()이 빠르다

# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys
from collections import deque

result = []


class Queue:
    def __init__(self):
        self.list = deque([])
        self.len = 0

    def push(self, x):
        self.list.append(x)
        self.len += 1

    def pop(self):
        if self.len == 0:
            result.append(-1)
        else:
            result.append(self.list[0])
            self.list.popleft()
            self.len -= 1

    def size(self):
        result.append(self.len)

    def empty(self):
        if self.len:
            result.append(0)
        else:
            result.append(1)

    def front(self):
        if self.len:
            result.append(self.list[0])
        else:
            result.append(-1)

    def back(self):
        if self.len:
            result.append(self.list[self.len - 1])
        else:
            result.append(-1)


n = int(sys.stdin.readline())

queue = Queue()

while n > 0:

    n -= 1
    splited_input = sys.stdin.readline().split()
    op = splited_input[0]

    if op == "push":
        queue.push(splited_input[1])
    elif op == "pop":
        queue.pop()
    elif op == "size":
        queue.size()
    elif op == "empty":
        queue.empty()
    elif op == "front":
        queue.front()
    elif op == "back":
        queue.back()

for i in result:
    print(i)


