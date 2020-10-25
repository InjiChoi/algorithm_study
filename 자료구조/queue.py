# 큐 구현
queue = list()

def enqueue(data):
    queue.append(data)

def dequeue():
    data = queue[0]
    del queue[0]
    return data
# or queue.pop(0)