# 스택 구현
stack = list()

def push(data):
    stack.append(data)

def pop():
    data = stack[-1]
    del stack[-1]
    return data
# or stack.pop()