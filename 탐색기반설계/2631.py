# 보물 찾기 -> 시간초과
# n, k = map(int, input().split())
# n_list = list(map(int, input().split()[:n]))

# count = 0
# temp = 0

# for i in range(0, n):
#     temp = n_list[i]

#     if n_list[i] == k :
#         count += 1
#         continue

#     else :
#         for j in range(i+1, n):
#             temp += n_list[j]
#             if (temp > k):
#                 break
#             elif (temp == k):
#                 count += 1
#                 break

# print(count)

n,k=map(int, input().split())
a=[0]
cnt=0
a[1:n]=[int(i) for i in input().split()]

for i in range(1, n+1) :
    a[i]+=a[i-1]

t=0
for i in range(1, n+1) :
    while a[i]-a[t]>k :
        t+=1
    if a[i]-a[t]==k :
        cnt+=1

print(cnt)