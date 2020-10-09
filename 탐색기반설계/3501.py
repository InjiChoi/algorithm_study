# RGB 거리 (Small)
from itertools import combinations as cb

n = int(input())
r = [0 for i in range(n)]
g = [0 for i in range(n)]
b = [0 for i in range(n)]

for i in range(n):
    r[i], g[i], b[i] = map(int, input().split())
# print(r, g, b) rgb 출력 확인

