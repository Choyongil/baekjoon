# 10866번 덱큐

# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys

results = []

class Deque:
    def __init__(self):
        self.list = []
        self.len = 0

    def push_front(self, x):
        self.list.insert(0, x)
        self.len += 1
        # print(self.list)

    def push_back(self, x):
        self.list.append(x)
        self.len += 1
        # print(self.list)

    def pop_front(self):
        if self.len:
            results.append(self.list.pop(0))
            self.len -= 1
        else:
            results.append(-1)

    def pop_back(self):
        if self.len:
            results.append(self.list.pop())
            self.len -= 1
        else:
            results.append(-1)

    def size(self):
        results.append(self.len)

    def empty(self):
        if not self.len:
            results.append(1)
        else:
            results.append(0)

    def front(self):
        if self.len:
            results.append(self.list[0])
        else:
            results.append(-1)

    def back(self):
        if self.len:
            results.append(self.list[-1])
        else:
            results.append(-1)


deque = Deque()

n = int(sys.stdin.readline())

while n > 0:
    n -= 1
    splited_order = sys.stdin.readline().split()

    op = splited_order[0]

    if op == 'push_front':
        deque.push_front(splited_order[1])
    elif op == 'push_back':
        deque.push_back(splited_order[1])
    elif op == 'pop_front':
        deque.pop_front()
    elif op == 'pop_back':
        deque.pop_back()
    elif op == 'size':
        deque.size()
    elif op == 'empty':
        deque.empty()
    elif op == 'front':
        deque.front()
    elif op == 'back':
        deque.back()

for result in results:
    print(result)