# 극장 좌석 배치 2.......
from itertools import combinations_with_replacement

n, k = map(int, input().split())
seat = [0 for i in range(n-2*k+1)]
count=0

for i in range(0,n-2*k+1):
    seat[i].append(i)
print(seat)
for i in combinations_with_replacement(seat, k+1):
    count +=1

print(count)