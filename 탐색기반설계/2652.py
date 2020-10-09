# 극장 좌석 배치 2.......
from itertools import combinations_with_replacement

n, k = map(int, input().split())
count=0
seat = []
for i in range(0,k+1):
    seat.append(i)
if n-2*k+1 > 0:
    for i in combinations_with_replacement(seat, n-2*k+1):
        count +=1
else:
    count=0
print(count)