# 사발 뒤집기 (tiny)
lst = list(map(int, input().split()[:8]))
# not(0) = True & not(1) = False
def flip(n):
    if n==0:
        lst[n] = not(lst[n-1])
        lst[n+1] = not(lst[n+1])
    elif n==7:
        lst[n-1] = not(lst[n-1])
        lst[n] = not(lst[n-1])
    else:
        lst[n-1] = not(lst[n-1])
        lst[n] = not(lst[n-1])
        lst[n+1] = not(lst[n+1])
tmp=0
cnt=0
while(True):
    for i in range(len(lst)):
        if lst[i] == 1:
            flip(i)
            cnt += 1
            for j in lst:
                tmp += j
                if tmp==0:
                    break
print(cnt)