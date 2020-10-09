# 랜선 자르기
from sys import stdin
# input 대신 stdin (시간 초과 방지)
k, n = map(int, stdin().readline.split())
lst = list(map(int, stdin.readlines()))
h, l = sum(lst)

while 1 <= h :
    mid = (h+1)//2
    count = sum([x//mid for x in lst])

    if count < n :
        h = mid - 1
    elif count >= n :
        l = mid + 1
        answer = mid

print(answer)