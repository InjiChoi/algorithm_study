# baekjoon 2164 카드2
import sys
from collections import deque

n = input(sys.stdin.readline())
queue = deque()

for i in range(n):
    queue.append(i+1)

while len(queue):
    queue.popleft()
    queue.append(queue.popleft())

print(queue.pop())