# 극장 좌석 배치 1
from itertools import combinations

n, k = map(int, input().split())
seat = [0 for i in range(n)]
count=0

for i in range(0,n):
    seat[i] = i

for i in combinations(seat, k):
    count +=1

print(count)