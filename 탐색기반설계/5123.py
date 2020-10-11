# 지원 vs 민서 (Small) 
from sys import stdin

n = int(input())
n_list = list(map(int,stdin.readline().split()))
lst = [0 for i in range(3)]

# cnt=0

# for i in range(len(n_list)):
#     for j in range(i+1, len(n_list)):
#         if (n_list[i]+n_list[j])%3==0:
#             cnt+=1
# print(cnt) => 시간초과

for i in range(len(n_list)):
    if n_list[i] % 3 == 0:
        lst[0] += 1
    elif n_list[i] % 3 == 1:
        lst[1] += 1
    else:
        lst[2] += 1
answer = int((lst[0]*(lst[0]-1))/2 + (lst[1]*lst[2]))
print(answer)