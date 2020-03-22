# BaekJoon 10828 stack

arr = []

class Stack:
    def __init__(self):
        self.len = 0
        self.list = []

    def push(self, x):
        self.list.append(x)
        self.len += 1

    def pop(self):
        if self.len == 0:
            arr.append(-1)
        else:
            arr.append(self.list[-1])
            del self.list[self.len - 1]
            self.len -= 1

    def top(self):
        if self.len == 0:
            arr.append(-1)
        else:
            arr.append(self.list[-1])

    def size(self):
        arr.append(self.len)

    def empty(self):
        if self.len:
            arr.append(0)
        else:
            arr.append(1)


num = int(input())

stack = Stack()

while (num > 0):
    num -= 1
    input_split = input().split()

    op = input_split[0]
    if op == "push":
        stack.push(input_split[1])
    elif op == "pop":
        stack.pop()
    elif op == "top":
        stack.top()
    elif op == "size":
        stack.size()
    elif op == "empty":
        stack.empty()

for i in range(len(arr)):
    print(arr[i])