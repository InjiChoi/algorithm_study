# Lower Bound
n, k = map(int, input().split())
n_list = list(map(int, input().split()[:n]))

count = 0

for i in n_list:
    count += 1
    if i >= k :
        break

if n_list[count-1] >= k:
    print(count)
else:
    print(count+1)