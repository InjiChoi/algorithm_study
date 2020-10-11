# 사냥꾼
from sys import stdin

# m, n, l = map(int, stdin().readline.split())
m, n, l = map(int, input().split())
m_list = list(map(int, input().split()[:m]))
n_list = [0 for i in range(n)]
cnt = 0 

for i in range(n):
    n_list[i] = list(map(int,input().split()))

for i in range(n):
    x = int(n_list[i][0])
    y = int(n_list[i][1])
    for j in range(m):
        x0 = int(m_list[j])
        if (x-x0)**2 + y**2 < l**2:
            cnt =+ 1

print(cnt)